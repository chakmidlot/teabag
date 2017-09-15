function main() {

    function clickListener() {
        document.getElementById('url-input').select();
        document.execCommand('copy');
    }

    document.getElementById('copy-btn').addEventListener('click', clickListener);

}
