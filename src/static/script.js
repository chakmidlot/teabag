function main() {

    var copyButton = document.getElementById('copy-btn');
    var inputToCopy = document.getElementById('input-to-copy');

    if (copyButton && inputToCopy) {
        copyButton.addEventListener('click', function() {
            inputToCopy.select();
            document.execCommand('copy');
        });
    }

}
