let auth1='b'
let auth2='c'
//probavamo2
window.onload=function(){
  let polja = document.querySelectorAll('.slovo1')
  eel.get_slova()(function(res){
	 polja.forEach((item, i) => {
		polja[i].innerHTML = res[i]
	 })
  })
  let polja2 = document.querySelectorAll('.slovo2')
  eel.get_slova()(function(res){
	 polja2.forEach((item, i) => {
		polja2[i].innerHTML = res[i]
	 })
  })
	eel.ubaci_igraca('Marko')(function(res){
		auth1=res
	})
	eel.ubaci_igraca('Sava')(function(res){
		auth2=res
	})

	let slovo1=document.querySelectorAll(".slovo1")
	let slovo2=document.querySelectorAll(".slovo2")
	const polje1=document.getElementById('donje-polje1')
	const polje2=document.getElementById('donje-polje2')
	const send1=document.getElementById('send1')
	const send2=document.getElementById('send2')

	slovo1.forEach(function(a){
		a.addEventListener('click', function(){
			polje1.insertAdjacentHTML('beforeEnd', a.innerHTML);
			a.disabled=true;
		})
	})
	slovo2.forEach(function(a){
		a.addEventListener('click', function(){
			polje2.insertAdjacentHTML('beforeEnd', a.innerHTML);
			a.disabled=true;
		})
	})
	send1.addEventListener('click', function(){
		eel.submit_word(auth1, polje1.innerHTML)
	})
	send2.addEventListener('click', function(){
		eel.submit_word(auth2, polje2.innerHTML)
	})

	document.getElementById("send2").addEventListener('click', function(){
		window.location = "mojbroj.html";
	});
	document.getElementById("go_skocko").addEventListener('click', function(){
		window.location = "skocko.html";
	});
}
