/**
 * "Report a bug" builds a report from the current transcript and opens it as a
 * pre-filled mail draft.
 *
 * The draft is deliberately not sent silently. A transcript can contain whatever
 * the person typed, so they get to read it and decide before it leaves their
 * machine. Sending without that step needs a server-side mail endpoint.
 */

const REPORT_EMAIL = "nikita.lipatov@gmail.com";

// mailto: URLs are truncated by browsers and mail clients well before the
// theoretical limit, so only the tail of a long conversation is carried.
const MAX_TRANSCRIPT_CHARS = 1500;

/**
 * Reads the rendered conversation back out of the DOM, in order.
 * @returns {Array<String>} one "[timestamp] Who: message" line per message
 */
function collectTranscript() {
    const nodes = document.querySelectorAll(
        "#chats .extra-info, #chats .extra-info-user, #chats .botMessage, #chats .userMessage"
    );

    const lines = [];
    let timestamp = "";

    nodes.forEach((node) => {
        const text = node.innerText.trim();
        if (!text) {
            return;
        }
        // Timestamps are rendered immediately before the message they belong to.
        if (node.classList.contains("extra-info") || node.classList.contains("extra-info-user")) {
            timestamp = text;
            return;
        }
        const who = node.classList.contains("userMessage") ? "User" : "Bot";
        lines.push(timestamp ? `[${timestamp}] ${who}: ${text}` : `${who}: ${text}`);
        timestamp = "";
    });

    return lines;
}

/**
 * Assembles the mail body: a prompt for the reporter, session details, and the
 * transcript.
 * @returns {String}
 */
function buildBugReport() {
    let transcript = collectTranscript().join("\n");
    let omitted = "";

    if (transcript.length > MAX_TRANSCRIPT_CHARS) {
        transcript = transcript.slice(-MAX_TRANSCRIPT_CHARS);
        omitted = "(earlier messages omitted so the draft fits in a mail link)\n\n";
    }

    return [
        "What went wrong?",
        "",
        "",
        "--- Session ---",
        `Reported:   ${getCurrentFormattedDateTime()}`,
        `Page:       ${window.location.href}`,
        `Connection: ${typeof ws !== "undefined" && ws ? readyStateName(ws.readyState) : "unavailable"}`,
        `Browser:    ${navigator.userAgent}`,
        "",
        "--- Transcript ---",
        omitted + (transcript || "(no messages yet)"),
    ].join("\n");
}

function readyStateName(state) {
    return ["connecting", "open", "closing", "closed"][state] ?? `unknown (${state})`;
}

/**
 * Briefly confirms the click. Opening a mail draft is invisible when the
 * machine has no mail client registered, which makes the button look dead.
 * @param {String} message
 */
function showReportNotice(message) {
    $(".report-notice").remove();
    const notice = $(`<div class="report-notice" role="status">${message}</div>`);
    notice.appendTo(".widget");
    setTimeout(() => notice.fadeOut(400, () => notice.remove()), 3200);
}

$(document).on("click", ".report-bug-open", async () => {
    const subject = "Chatbot bug report";
    const body = buildBugReport();

    // The report also goes on the clipboard, so it survives a machine with no
    // mail client and can be pasted into a ticket instead.
    let copied = false;
    try {
        await navigator.clipboard.writeText(`To: ${REPORT_EMAIL}\nSubject: ${subject}\n\n${body}`);
        copied = true;
    } catch (error) {
        console.log("Clipboard unavailable for the bug report.", error);
    }

    showReportNotice(
        copied
            ? "Opening your mail app. The report is also on your clipboard."
            : "Opening your mail app with the report."
    );

    window.location.href =
        `mailto:${REPORT_EMAIL}` +
        `?subject=${encodeURIComponent(subject)}` +
        `&body=${encodeURIComponent(body)}`;
});
