// Sinxron funksiyalar
function sinxron() {
    console.log("Sinxron vazifa boshlandi...");
    for (let i = 0; i < 5; i++) {
        console.log(`Hisoblash: ${i}`);
    }
    console.log("Sinxron tugadi!");
}

// Asinxron funksiyalar
async function asinxron() {
    console.log("Asinxron boshlandi...");

    try {
        // API so‘rovi (5 soniya kutadi)
        const response = await new Promise((resolve) => 
            setTimeout(() => resolve("API ma'lumotlari olindi!"), 5000)
        );
        console.log(response);
    } catch (error) {
        console.error("Xato: ", error);
    }

    console.log("Asinxron tugadi!");
}


console.log("Dastur boshlandi!");
sinxron();    // Sinxron funksiya
asinxron();   // Asinxron funksiya
console.log("Dastur tugadi!");
