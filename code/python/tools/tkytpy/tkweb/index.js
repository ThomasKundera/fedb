
function populateVideoList(obj) {
  const videodiv = document.querySelector("#videodiv");
  videodiv.innerHTML = "";
  const ytvlist = obj.ytvlist;

  const myli = document.createElement("li");
  for (const ytv of ytvlist) {
    const myul = document.createElement("ul");
    const mya = document.createElement("a");
    mya.textContent = ytv.title;
    mya.setAttribute('href',ytv.url)
    myul.appendChild(mya)
    myli.appendChild(myul)
  }
  videodiv.appendChild(myli);
}


const form = document.querySelector("#addytvideo");

async function sendData() {
  // Associate the FormData object with the form element
  const formData = new FormData(form);

  try {
    const response = await fetch("http://localhost:8000/post", {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify((Object.fromEntries(formData)))
    });
    const yidtext = await response.text();
    const yidjson=JSON.parse(yidtext);
    populateVideoList(yidjson);

  } catch (e) {
    console.error(e);
  }
}

// Take over form submission
form.addEventListener("submit", (event) => {
  event.preventDefault();
  sendData();
});
