function submit() {
	var givin, result;
	givin = document.getElementById("pass").value;
	if (givin == "flag:12345678") {
		result = "Well done";
	}
	else {
		result = "Incorrect";
	}
	document.getElementById("result").innerHTML = result;
}