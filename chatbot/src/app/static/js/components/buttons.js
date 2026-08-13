/**
 * Escape text that came from the server before it goes into markup.
 *
 * The server controls these strings today, but building HTML by concatenation
 * is exactly where that stops being true quietly.
 */
function escapeHtml(value) {
    return $("<div>").text(value).html();
}

/**
 * Render a collapsible group of choices.
 *
 * The group arrives as {label, options:[{label, command}]}. This used to be a
 * literal HTML string with one hardcoded entry, shown only because the greeting
 * carried a magic "default" payload; now any reply can offer a menu and the
 * contents come from whichever mode built it.
 */
function addButtons(group) {
    if (!group || !group.options || group.options.length === 0) {
        return;
    }

    setTimeout(() => {
        const options = group.options
            .map(
                (option) =>
                    `<li class="buttonTmplContentChild choice" data-command="${escapeHtml(option.command)}">` +
                        escapeHtml(option.label) +
                    "</li>"
            )
            .join("");

        $(
            '<div class="chat-list">' +
                '<div class="singleCardNew">' +
                    '<div class="buttons">' +
                        '<div class="menuNew"></div>' +
                    '</div>' +
                '</div>' +
            '</div>'
        )
        .appendTo(".chats")
        .hide()
        .fadeIn(1000);

        $(
            '<a class="action-button">' +
                `<li class="buttonTmplContentChild outer-child">${escapeHtml(group.label)}</li>` +
                `<ul class="action-button-inner hidden">${options}</ul>` +
            "</a>"
        ).appendTo(".menuNew");

        addEvent();
        scrollToBottomOfResults();
    }, 1000);
}

function addEvent() {
    $(".outer-child").off("click").on("click", function() {
        let target = $(this).next("ul").toggleClass("hidden");
        scrollToBottom(target);
    });

    function scrollToBottom(element) {
        if (!element.length || element.hasClass("hidden")) {
            return;
        }
        let container = $(".chats");
        let containerOffSet = container.offset().top;
        let elementOffSet = element.offset().top;
        let currentScroll = container.scrollTop();
        let newScroll = currentScroll + (elementOffSet - containerOffSet);
        container.animate({
            scrollTop: newScroll
        }, 500);
    }

    // Clicking a choice sends its command as though it had been typed.
    $(".choice").off("click").on("click", function() {
        const command = $(this).attr("data-command");
        setUserResponse(command);
        send(command);
    });
}

$(document).on("click", ".menu .menuChips", function() {
    const text = this.innerText;
    const payload = this.getAttribute("data-payload");
    setUserResponse(text);
    send(payload);
});
