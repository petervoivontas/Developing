const apiKey = 'AIzaSyCphjqEn7sVUUe_J-j3u7ilWGtn_KHuV5k';
const url = 'https://www.googleapis.com/urlshortener/v1/url';
const inputField = $('#inputField');
const resultField = $('#resultField');
const expandButton = $('#expandButton');
const shortenButton = $('#shortenButton');

function expandUrl () {
    const urlToExpand = url + '?key=' + apiKey + '&shortUrl=' + inputField.val();
    $.ajax({
        url: urlToExpand,
        type: 'GET',
        dataType: 'json',
        success (response) {
            resultField.text(response.longUrl);
            console.log(response);
        },
        error (jqXHR, status, errorThrown) {
            console.log(jqXHR);
            resultField.text('The request has returned an error');
        }
    });
}

function shortenUrl () {
    const urlToShorten = url + '?key=' + apiKey;
    $.ajax({
        url: urlToShorten,
        type: 'GET',
        data: JSON.stringify({longUrl: inputField.val()}),
        dataType: 'json',
        contentType: 'application/json',
        success (response) {
            console.log(response);
            resultField.text(response.id);
        },
        error (jqXHR, status, errorThrown) {
            console.log(jqXHR);
        }
    });
}

expandButton.click(expandUrl);
shortenButton.click(shortenUrl);