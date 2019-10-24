function randomBackground() {
	var bg = ["defaultBG","enableBG1","enableBG2"];
	var number = (Math.floor(Math.random() * bg.length) + 1)-1;
	console.log(number);
	document.getElementById('bg').classList.add(bg[number]);
	console.log(bg[number]);
}
