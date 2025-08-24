
000 so‘mdan kam bo‘lsa: foiz 5%
* 100000 - 500000 so‘m oralig‘ida bo‘lsa: foiz 7%
* 500000 so‘mdan katta bo‘lsa: foiz 10%

**Test case-lar:**

| Input  | Output |
| ------ | ------ |
| 50000  | 5%     |
| 100000 | 7%     |
| 300000 | 7%     |
| 600000 | 10%    |
| 99999  | 5%     |

---

### 🔹 **6. Telefon raqami operatorini aniqlash**

**Vazifa:**
Foydalanuvchidan telefon raqamini kiriting (masalan: 90xxxxxxx).
Raqam boshidagi kodga qarab operatorni aniqlang:

* 90, 91 — Ucell
* 93, 94 — Beeline
* 95, 97 — Uzmobile
* 88, 99 — Mobiuz
* Boshqalar — noma’lum operator

**Test case-lar:**

| Input     | Output            |
| --------- | ----------------- |
| 909876543 | Ucell             |
| 931234567 | Beeline           |
| 959876543 | Uzmobile          |
| 881234567 | Mobiuz            |
| 921234567 | Noma’lum operator |

---

### 🔹 **7. Email manzilini tekshirish**

**Vazifa:**
Foydalanuvchidan email manzilini kiriting.
Email manzili quyidagi shartlarni qanoatlantirishi kerak:

* @ belgisi bo‘lishi
* @ dan keyin nuqta (.) bo‘lishi
* Bo‘sh joy bo‘lmasligi

Agar shartlar bajarilsa — "Email manzili to‘g‘ri", aks holda "Email manzili noto‘g‘ri" deb chiqarilsin.

**Test case-lar:**

| Input                                       | Output                  |
| ------------------------------------------- | ----------------------- |
| [user@example.com](mailto:user@example.com) | Email manzili to‘g‘ri   |
| userexample.com                             | Email manzili noto‘g‘ri |
| user\@ex ample.com                          | Email manzili noto‘g‘ri |
| user\@examplecom                            | Email manzili noto‘g‘ri |

---

### 🔹 **8. Son oraliqda yoki emas**

**Vazifa:**
Foydalanuvchidan son kiriting.
Agar son 10 dan katta va 100 dan kichik bo‘lsa "Oraliqda" deb chiqarilsin, aks holda "Oraliqda emas".

**Test case-lar:**

| Input | Output        |
| ----- | ------------- |
| 50    | Oraliqda      |
| 9     | Oraliqda emas |
| 101   | Oraliqda emas |

---

### 🔹 **9. Uchburchak turi**

**Vazifa:**
Foydalanuvchidan uchta tomon uzunligini kiriting. Ularni asos qilib, uchburchak teng tomonli, teng yonli yoki turli tomonli ekanligini aniqlang.

**Test case-lar:**

| Input   | Output        |
| ------- | ------------- |
| 5, 5, 5 | Teng tomonli  |
| 5, 5, 7 | Teng yonli    |
| 3, 4, 5 | Turli tomonli |

---

### 🔹 **10. Ballar bo‘yicha baho**

**Vazifa:**
Foydalanuvchidan imtihon ballini kiriting (0 dan 100 gacha). Quyidagi baholash tizimiga asoslanib, bahoni chiqarilsin:

* 90-100 — “A”
* 80-89 — “B”
* 70-79 — “C”
* 60-69 — “D”
* 0-59 — “F”

**Test case-lar:**

| Input | Output |
| ----- | ------ |
| 95    | A      |
| 82    | B      |
| 75    | C      |
| 65    | D      |
| 50    | F      |

---

### 🔹 **11. Yilning faslini aniqlash**

**Vazifa:**
Foydalanuvchidan oy raqamini (1 dan 12 gacha) kiriting. Oyga qarab faslni aniqlang:

* 12, 1, 2 — Qish
* 3, 4, 5 — Bahor
* 6, 7, 8 — Yoz
* 9, 10, 11 — Kuz

**Test case-lar:**

| Input | Output |
| ----- | ------ |
| 1     | Qish   |
| 4     | Bahor  |
| 7     | Yoz    |
| 10    | Kuz    |

---

### 🔹 **12. Parollar mos keladimi?**

**Vazifa:**
Foydalanuvchidan ikki marta parol kiriting. Agar parollar bir xil bo‘lsa “Parol qabul qilindi”, aks holda “Parollar mos emas” deb chiqarilsin.

**Test case-lar:**

| Input              | Output              |
| ------------------ | ------------------- |
| “abc123”, “abc123” | Parol qabul qilindi |
| “12345”, “54321”   | Parollar mos emas   |


