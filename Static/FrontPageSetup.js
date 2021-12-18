
document.getElementById("subtext").innerHTML = "Applied statistics graduate | Improving programming repertoire | DevOps Engineer at APG"

let start_index = 0
function giveWords(){
	let words = "DevOps;Azure;CI/CD;Docker;Utrecht University;The Hague;Msc. Statistics;Bsc. Psychologie;Data-science;Simulations;Cloud Computing;HTML;CSS;Python;Java;Javascript;Developer;Netherlands;SQL;Azure;Machine Learning;Deep Learning;R;R-Studio;Visual Studio Code;Pycharm;Active Directory;Git;Github;Keras;Tensorflow;Game Development;Artifical Intelligence;Tesla;Compliancy;Working-Out;CBS;Big Data;Alteryx;Qlik"
	array = words.split(";")
	return array
	
}
wordsArray = giveWords()
let totalGravel = wordsArray.length

setupGravel()

function setupGravel(){
	let container = document.getElementById("oncomming")
	for(i = 0; i < totalGravel; i++){
		
		
		
		
		let position = start_index*100 + Math.random()*100-150
		start_index++
		if(start_index == 3){
			start_index = 0
		}
		
		
		let delay = 4.5 + Math.random()*30
		
		
		container.appendChild(createGravel(position,delay,i,wordsArray[i]))
		
	}
	
	
}





function createGravel(position, delay,index,word){
	let id = "gravel_".concat(index.toString(10))
	gravelElem = document.createElement("div")
	gravelElem.className = "gravel"
	gravelElem.id = id
	
	let animation_duration =  Math.log(Math.abs(position-50)*15000000)/2
	
	gravelElem.style.left = position.toString(10).concat("vw")
	//gravelElem.style.animationDuration = animation_duration.toString(6).concat("s")
	//let shadowAngle = 26*(position - 50)/200
	
	gravelElem.style.width = "12rem"
	gravelElem.innerHTML = word
	gravelElem.style.zIndex = "300"
		
	
	
			
	gravelElem.style.animationDelay = delay.toString(10).concat("s")
		
	return gravelElem
	
	
}




