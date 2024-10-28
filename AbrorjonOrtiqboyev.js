class Queue {
    constructor() {
      this.navbat = [];
    }
  
    // Element qo'shish
    add(element) {
      this.navbat.push(element);
    }
  
    // Element o'chirish
    delete() {
      if (!this.isEmpty()) {
        return "Navbat bo'sh";
      }
      return this.navbat.shift();
    }
  
    // Birinchi element
    first() {
      if (!this.isEmpty()) {
        return "Navbat bo'sh";
      }
      return this.navbat[0];
    }
  
    // Bo'shligini tekshirish
    isEmpty() {
        if (this.navbat.length) {
            return true
        } 
        else{
            return false
        }
    }
  
    // Navbat uzunligini
    size() {
      return this.navbat.length;
    }
  
    // Navbatdagi barcha elementlarni ko'rish
    printAll() {
      return this.navbat.join(" ");
    }
  }
  
  // Foydalanish:
  const yangiNavbat = new Queue();
  
  // Yanagi element qo'shish
  yangiNavbat.add(10);
  yangiNavbat.add(20);
  yangiNavbat.add(30);
  
  console.log("Navbatning barcha elementlari: ", yangiNavbat.printAll())
  console.log("Navbatni birinchi elementi: ", yangiNavbat.first())
  console.log("Navbat uzunligi: ", yangiNavbat.size())
  console.log("Navbatdan o'chirilgan element: ", yangiNavbat.delete())
  console.log("Navbatning barcha elementlari: ", yangiNavbat.printAll())

  