const apiKey = 'AIzaSyCphjqEn7sVUUe_J-j3u7ilWGtn_KHuV5k';
const url = 'https://www.googleapis.com/urlshortener/v1/url';
const inputField = $('#inputField');
const resultField = $('#resultField');
const expandButton = $('#expandButton');
const shortenButton = $('#shortenButton');

function expandUrl () {
    const urlToExpand = url + '?key=' + apiKey + '&shortUrl=' + inputField.val();
    const xhr = new XMLHttpRequest();
    xhr.responseType = 'json';
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            console.log(xhr.response);
            resultField.text(xhr.response.longUrl);
        }
    }
    xhr.open('GET', urlToExpand);
    xhr.send();
}

function shortenUrl () {
    const urlWithKey = url + '?key=' + apiKey;
    const urlToShorten = inputField.val();
    const data = JSON.stringify({longUrl: urlToShorten});
    const xhr = new XMLHttpRequest();
    xhr.responseType = 'json';
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            console.log(xhr.response);
        }
    }
    xhr.open('POST', urlWithKey);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(data);
}

expandButton.click(expandUrl);
shortenButton.click(shortenUrl);