function c(val)
{
	document.getElementById("display").value = val;
}

function math(val)
{
	document.getElementById("display").value += val;
}

function e()
{
	try{
		c(eval(document.getElementById("display").value))
	}
	catch(e){
		c("Error")
	}
}

function histogram()
{
	var history = document.getElementById("display").value;
	var element = document.getElementById("histogram");

	var div = document.createElement("div");
	div.className = "history";
	div.innerHTML = history;
	
	if(history != "")
	{

		element.insertBefore(div, element.childNodes[0]);	
	}
	
	//document.getElementById("history").innerHTML = history;
}

function myClear()
{
	var elem = document.getElementsByClassName('history');
	 elem.parentNode.removeChild(elem);
}
