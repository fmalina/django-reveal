function $e(Id){
	return document.getElementById(Id);
}

function reveal(url, info_attr, protocol){
	var xhr = new XMLHttpRequest();
	xhr.open('GET', url, true);
	xhr.onreadystatechange = function(){
		if(xhr.readyState==4){
			data = xhr.responseText;
			var place = $e('pull'+info_attr);
			if(data=='login'){
				window.location = '/login/?next=' + window.location.pathname;
			} else {
				place.innerHTML = data;
				place.href = protocol + data;
				place.classList.remove('disabled');
				console.log(window.location.href);
			}
		}
	}
	xhr.send();
}
