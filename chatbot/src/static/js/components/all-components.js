function include(file) {
    const script = document.createElement('script');

    script.src = file;
    script.type = 'text/javascript';
    script.defer = true;

    document.getElementsByTagName('head').item(0).appendChild(script);
}

include(`/${srcName}/js/components/buttons.js`)
include(`/${srcName}/js/components/chat.js`)
include(`/${srcName}/js/components/table.js`)