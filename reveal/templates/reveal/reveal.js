function reveal(url, info_attr, protocol, identifier){
	var xhr = new XMLHttpRequest();
	xhr.open('GET', url, true);
	xhr.onreadystatechange = function(){
		if(xhr.readyState==4){
			data = xhr.responseText;
			var place = document.getElementById(identifier);
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
