function getYouTubeVideoTitle(videoId, elementId) {
    var request = new XMLHttpRequest();
    var apiKey = 'AIzaSyCDskVh1aRW-u1FPkxml7GNWm6CKWvpbcE';

    request.open('GET', 'https://www.googleapis.com/youtube/v3/videos?id=' + videoId + '&key=' + apiKey + '&part=snippet', true);
    request.onload = function () {
        if (request.status >= 200 && request.status < 400) {
            var response = JSON.parse(request.responseText);
            var videoTitle = response.items[0].snippet.title;
            document.getElementById(elementId).textContent = videoTitle;
        } else {
            console.error('Đã xảy ra lỗi khi gửi yêu cầu đến YouTube API.');
        }
    };

    request.onerror = function () {
        console.error('Đã xảy ra lỗi kết nối.');
    };

    request.send();
}

function updateVideoTitles() {
    var elements = document.getElementsByClassName('vid__title');
    for (var i = 0; i < elements.length; i++) {
        var element = elements[i];
        var elementId = element.id;
        getYouTubeVideoTitle(elementId, elementId)
    }
}