// define function to import js file
function include(file) {
    const script = document.createElement('script');

    script.src = file;
    script.type = 'text/javascript';
    script.defer = true;

    document.getElementsByTagName('head').item(0).appendChild(script);
}

// import components
include(`/${srcName}/js/components/all-components.js`)

document.addEventListener('DOMContentLoaded', () => {
    localStorage.clear();
    console.log("Local Storage has been cleared.");
});

window.addEventListener('load', () => {
    $(document).ready(() => {
        // Clear sessionStorage on page on load
        sessionStorage.removeItem("lastUtterance");
        // initial conversation
        // method name and message is imported from chat.js
        setBotResponse(GREETING);

        $(".scroll-to-top").click(function() {
            $(".chats").animate({scrollTop: 0}, 'slow');
        });

        $(".chats").scroll(function(data) {
            if ($(".chats").scrollTop() > 60) {
                $(".chatbox-header-logo").hide();
                $(".scroll-to-top").fadeIn();
            } else {
                $(".chatbox-header-logo").show();
                $(".scroll-to-top").fadeOut();
            }
        });

        let myDate = new Date();
        let hours = myDate.getHours();
        let greet;
        if (hours >= 7 && hours < 12) {
            greet = "Good Morning!";
        } else if (hours >= 12 && hours <= 17) {
            greet = "Good Afternoon!";
        } else if (hours >= 18 && hours <= 22) {
            greet = "Good Evening!";
        } else {
            greet = "Good Night!"
        }
        $("#salutation").text(`${greet} ${userName}`);
        // make widget draggable
        $(".widget").draggable({handle: '.chatbox-header', containment: 'window'});
    });

    // open chatbox window
    $(".chat-button").click(() => {
        $(".chat-button").toggle();
        $(".widget").toggle();
    })

    // close chatbox window
    $(".minimize-btn").click(() => {
        $(".chat-button").toggle();
        $(".widget").toggle();
        scrollToBottomOfResults();
    });

    // expand chatbox window
    $(".expand-btn").click(() => {
        $(".widget").toggleClass("expanded");
    });

});