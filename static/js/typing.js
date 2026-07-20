const words = [
    "Python Developer",
    "Flask Developer",
    "AI & Data Analytics Enthusiast"
];

let i = 0;
let j = 0;
let currentWord = "";
let isDeleting = false;

function type() {

    currentWord = words[i];

    if (!isDeleting) {

        document.getElementById("typing").textContent =
            currentWord.substring(0, j++);

        if (j > currentWord.length) {

            isDeleting = true;

            setTimeout(type, 1200);

            return;
        }

    } else {

        document.getElementById("typing").textContent =
            currentWord.substring(0, j--);

        if (j === 0) {

            isDeleting = false;

            i = (i + 1) % words.length;

        }

    }

    setTimeout(type, isDeleting ? 50 : 100);

}

type();