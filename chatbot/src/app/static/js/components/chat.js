const converter = new showdown.Converter();

// No buttons here: menus are something a reply offers, not something the first
// message hardcodes. Type `type` to see one.
const GREETING = [{
    "text": "Hey, I'm here to help you. Please type 'help' to see what I can do for you.",
}];

function scrollToBottomOfResults() {
    const terminalResultDiv = document.getElementById("chats");
    terminalResultDiv.scrollTop = terminalResultDiv.scrollHeight;
}

$(".reload-btn").click(() => {
    // destroy the existing chart
    $(".collapsible").remove();
    if (typeof chatChart !== "undefined") {
        chatChart.destroy();
    }
    $(".chart-container").remove();
    if (typeof modalChart !== "undefined") {
        modalChart.destroy();
    }
    // clean chats history
    $(".chats").html("");
    $(".userInput").val("");
    // output chat greeting
    setBotResponse(GREETING);
});

$(".userInput").on("keyup keypress", (e) => {
    const keyCode = e.keyCode || e.which;

    const text = $(".userInput").val();
    // Shift+Enter inserts a newline; plain Enter sends.
    if (keyCode === 13 && !e.shiftKey) {
        if (text === "" || $.trim(text) === "") {
            e.preventDefault();
            return false;
        }
        // destroy existing chart
        $(".collapsible").remove();
        $(".dropDownMsg").remove();
        if (typeof chatChart !== "undefined") {
            chatChart.destroy();
        }
        $(".chart-container").remove();
        if (typeof modalChart !== "undefined") {
            modalChart.destroy();
        }

        $(".userInput").blur();
        setUserResponse(text);
        send(text);

        e.preventDefault();
        return false;
    }
    return true;
});

/**
 * Set user response on the chat screen
 * @param {String} message
 */
function setUserResponse(message) {
    const user_response =
        `<div aria-live="off" class="extra-info-user">${getCurrentFormattedDateTime()}</div>` +
        `<img class="userAvatar" src='/chatbot/static/img/userIcon.png' height="32" width="32"/>` +
        `<p class="userMessage">${message}</p>` +
        `<div class="clearfix"></div>`;
    $(user_response).appendTo(".chats").show("slow");

    $(".userInput").val("");
    scrollToBottomOfResults();
    showBotTyping();
}

/**
 * Renders bot response on to the chat screen
 * @param {Array} response json array containing different types of bot response
 */
function setBotResponse(response) {

    setTimeout(() => {
        hideBotTyping();

        console.log(response);

        if (response.length < 1) {
            const fallbackMessage = "I cannot find any results now, please try again later!";

            const botResponse =
                `<div aria-live="off" class="extra-info">${getCurrentFormattedDateTime()}</div>` +
                `<img class="botAvatar" src="/chatbot/static/img/botIcon.png" height="32" width="32" />` +
                `<p class="botMessage">${fallbackMessage}</p>` +
                `<div class="clearfix"></div>`;
            $(botResponse).appendTo(".chats").hide().fadeIn(1000);
            scrollToBottomOfResults();
        } else {
            for (let i = 0; i < response.length; i += 1) {
                if (Object.hasOwnProperty.call(response[i], "text")) {
                    if (response[i].text != null) {
                        let botResponse;
                        let html = converter.makeHtml(response[i].text);
                        html = html
                            .replaceAll("<p>", "")
                            .replaceAll("</p>", "");
                        html = html.replace(/(?:\r\n|\r|\n)/g, "<br>");

                        // check for list text
                        if (
                            html.includes("<ul") ||
                            html.includes("<ol") ||
                            html.includes("<li") ||
                            html.includes("<h3") ||
                            html.includes("<b")
                        ) {
                            botResponse = getBotResponse(html);
                        } else {
                            // if no markdown is found, render text as is
                            if (!botResponse) {
                                botResponse =
                                    `<div aria-live="off" class="extra-info">${getCurrentFormattedDateTime()}</div>` +
                                    `<img class="botAvatar" src="/chatbot/static/img/botIcon.png" height="32" width="32" />` +
                                    `<p class="botMessage">${response[i].text}</p>` +
                                    `<div class="clearfix"></div>`;
                            }
                        }

                        $(botResponse).appendTo(".chats").hide().fadeIn(1000);
                    }
                }

                if (Object.hasOwnProperty.call(response[i], "buttons")) {
                    addButtons(response[i].buttons);
                }
                if (Object.hasOwnProperty.call(response[i], "table")) {
                    let clickable = true;
                    if (Object.hasOwnProperty.call(response[i], "clickable")) {
                        if (typeof response[i].clickable !== 'undefined') {
                            clickable = (response[i].clickable === 'true');
                        }
                    }

                    if (response[i].table.length > 0) {
                        addTable(response[i].table, clickable);
                    }

                }
            }
            scrollToBottomOfResults();
        }

        $(".userInput").focus();
    }, 500);
}

/**
 * Returns formatted bot response.
 * @param {String} text bot message response's text
 */
function getBotResponse(text) {
    const botResponse =
        `<div aria-live="off" class="extra-info">${getCurrentFormattedDateTime()}</div>` +
        `<img class="botAvatar" src="/chatbot/static/img/botIcon.png" height="32" width="32" />` +
        `<span class="botMessage">${text}</span>` +
        `<div class="clearfix"></div>`;
    return botResponse;
}

function getCurrentFormattedDateTime() {
    const now = new Date();
    // Get days of week abbrevation
    const daysOfWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    const dayOfWeek = daysOfWeek[now.getDay()];

    // Get month abbrevation
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Now", "Dec"]
    const month = months[now.getMonth()];

    const day = now.getDate();
    const year = now.getFullYear();
    let hours = now.getHours();
    const isPM = hours >= 12;
    hours = hours % 12 || 12;
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const apm = isPM ? "PM" : "AM";
    return `${dayOfWeek} ${month} ${day} ${year} at ${hours}:${minutes} ${apm}`
}

/**
 * Removes the bot typing indicator from the chat screen.
 */
function hideBotTyping() {
    $("#botAvatar").remove();
    $(".botTyping").remove();
}

/**
 * Adds the bot typing indicator from the chat screen.
 */
function showBotTyping() {
    const botTyping =
        `<img class="botAvatar" id="botAvatar" src="/chatbot/static/img/botIcon.png" height="32" width="32"/>` +
        `<div class="botTyping">` +
            `<div class="bounce1"></div>` +
            `<div class="bounce2"></div>` +
            `<div class="bounce3"></div>` +
        `</div>`;
    $(botTyping).appendTo(".chats");
    $(".botTyping").show();
    scrollToBottomOfResults();
}

function sendMessage(payload) {
    if (ws && ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify(payload));
    } else {
        console.log("Websocket is not open!")
    }
}

// One renderer per template_type. Adding a message shape means adding an entry
// here and a builder in messages.py -- the two ends of the same contract.
const MESSAGE_RENDERERS = {
    text: (message) => ({ text: message.text }),
    table: (message) => ({
        text: message.text,
        clickable: message.clickable,
        table: message.msg_payload,
    }),
    choices: (message) => ({
        text: message.text,
        buttons: { label: message.label, options: message.msg_payload },
    }),
};

ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    const message = data && data.message;

    if (!message) {
        console.error("Received a reply with no message", data);
        return;
    }

    const render = MESSAGE_RENDERERS[message.template_type];
    if (!render) {
        // Previously this produced an empty array, which rendered as "I cannot
        // find any results now" -- an unrelated-looking error for what is
        // really a missing renderer.
        console.error("No renderer for template_type", message.template_type, message);
        setBotResponse([{ text: "I do not know how to display that reply." }]);
        return;
    }

    setBotResponse([render(message)]);
}

/**
 * Sends the user message to the server.
 *
 * The raw text goes as-is: the server decides which mode handles it. Mapping
 * text to a mode here would mean the browser could silently drop anything it
 * did not recognise, which is exactly what this used to do.
 *
 * @param {String} message - user message
 */
async function send(message) {
    await new Promise((r) => setTimeout(r, 2000));

    sendMessage({ type: "user", text: message });
}
