document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".nav-link");
    const contents = document.querySelectorAll(".tab-content");

    tabs.forEach(tab => {
      tab.addEventListener("click", function () {
        const target = this.getAttribute("data-tab");
        if (target) {
          tabs.forEach(t => t.classList.remove("active"));
          contents.forEach(c => c.classList.remove("active"));
          this.classList.add("active");
          document.getElementById(target).classList.add("active");
        }
      });
    });
  });
  function searchUsers() {
    let input = document.getElementById("searchUser").value.toLowerCase();
    let userCards = document.getElementById("userList").getElementsByClassName("user-card");

    for (let i = 0; i < userCards.length; i++) {
      let name = userCards[i].getElementsByTagName("h5")[0].innerText.toLowerCase();
      if (name.includes(input)) {
        userCards[i].parentElement.style.display = "";
      } else {
        userCards[i].parentElement.style.display = "none";
      }
    }
  }

  
  function showEventDetails(name, date, venue, posterUrl) {
    document.getElementById('eventTitle').innerText = name;
    document.getElementById('eventDate').innerText = date;
    document.getElementById('eventVenue').innerText = venue;

    // Update the modal image (if needed)
    let modalImage = document.createElement("img");
    modalImage.src = posterUrl;
    modalImage.style.width = "100%";
    modalImage.style.borderRadius = "10px";

    // Insert the image at the top of the modal body
    let modalBody = document.querySelector('.modal-body');
    modalBody.innerHTML = ""; // Clear previous content
    modalBody.appendChild(modalImage);

    // Append event details
    modalBody.innerHTML += `<p><strong>Date:</strong> ${date}</p>`;
    modalBody.innerHTML += `<p><strong>Venue:</strong> ${venue}</p>`;
}