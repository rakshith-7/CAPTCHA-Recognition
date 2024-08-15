// API call is made on clicking the submit button
document.getElementById("submit").addEventListener("click", () => {
  const URL =
    "http://127.0.0.1:5000/captcha_image";


  const APIobj = {  };
  const APIjson = JSON.stringify(APIobj);
  console.log(APIjson);

  async function f() {
    var finalData;

    const rawResponse = await fetch(URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: APIjson
    })
      .then(data => {
        finalData = data.json();
      })
      .catch(err => {
        console.log(err);
      });

    console.log(finalData);
    return finalData;
  }

  const apiData = f();

  apiData.then(workingData => {
    // fetching the API output and communicating with the front-end
    document.getElementById("para-1").innerHTML = workingData.predicted_output;
  });
});

const fileupload = document.getElementById("fileupload");
const savebutton = document.getElementById("savebutton");

// This code is basically used when a user wants to upload an image i.e captcha image
var uploadedfile;
fileupload.addEventListener('change', function(e) {
  console.log(e.target.files[0]);
  uploadedfile = e.target.files[0];
} )

savebutton.addEventListener('click', async function() {
  const formData = new FormData();
  formData.append('image', uploadedfile);
  await fetch("http://127.0.0.1:5000/fileupload", {
    method : 'POST',
    body : formData
  })
  .then(console.log("file uploaded"))
  .catch((e) => console.log(e));
})


