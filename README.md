# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Seiring pertumbuhan bisnisnya, perusahaan menghadapi tantangan besar dalam mempertahankan karyawan. Perusahaan Jaya Jaya Maju ini masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Tingginya tingkat attrition (pengunduran diri karyawan) mengakibatkan tingginya biaya rekrutmen dan pelatihan, serta terganggunya stabilitas tim dan produktivitas organisasi. Sehingga perusahaan perlu melakukan analisa untuk mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut.

### Permasalahan Bisnis
Tujuan:
- Mengidentifikasi faktor-faktor yang memengaruhi attrition rate karyawan di Jaya Jaya Maju.
- Menyediakan dashboard interaktif agar HR dapat memantau kondisi tenaga kerja secara real-time.

Problem Statements:
- Apa saja faktor signifikan yang mendorong keputusan karyawan untuk keluar dari perusahaan?
- Bagaimana persebaran attrition di berbagai divisi, usia, jabatan, dan tingkat gaji?
- Bagaimana visualisasi data dapat membantu HR dalam mendeteksi area berisiko tinggi attrition?

Seluruh Permasalahan Bisnis yang Diselesaikan (Goals):
- Memprediksi karyawan mana yang memiliki potensi resign.
- Menyajikan data visual tentang faktor-faktor risiko seperti usia, gaji, masa kerja, dan jenjang karir.
- Memberikan rekomendasi tindakan preventif berdasarkan hasil analisis data.

### Cakupan Proyek
- Eksplorasi dan pembersihan data HR karyawan.
- Transformasi data (handling missing values, outliers, encoding, scaling, log transformasi untuk fitur skewed).
- Pemodelan prediksi attrition menggunakan beberapa model ML (Logistic Regression, Decision Tree, Random Forest, XGBoost, dan Neural Network).
- Evaluasi performa model dengan metrik klasifikasi.
- Visualisasi hasil prediksi dalam bentuk dashboard menggunakan Metabase dan Streamlit.

### Persiapan

Sumber data : [Employee Data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee).<br>
Data diambil dari Dataset internal dari Jaya Jaya Maju terkait informasi demografis dan pekerjaan karyawan. 

Berikut penjelasan mengenai fitur yang akan diambil : 
* **EmployeeId** - Employee Identifier
* **Attrition** - Did the employee attrition? (0=yes, 1=no)
* **Age** - Age of the employee
* **BusinessTravel** - Travel commitments for the job
* **DailyRate** - Daily salary
* **Department** - Employee Department
* **DistanceFromHome** - Distance from work to home (in km)
* **Education** - 1-Below College, 2-College, 3-Bachelor, 4-Master,5-Doctor
* **EducationField** - Field of Education
* **EnvironmentSatisfaction** - 1-Low, 2-Medium, 3-High, 4-Very High
* **Gender** - Employee's gender
* **HourlyRate** - Hourly salary
* **JobInvolvement** - 1-Low, 2-Medium, 3-High, 4-Very High
* **JobLevel** - Level of job (1 to 5)
* **JobRole** - Job Roles
* **JobSatisfaction** - 1-Low, 2-Medium, 3-High, 4-Very High
* **MaritalStatus** - Marital Status
* **MonthlyIncome** - Monthly salary
* **MonthlyRate** - Mounthly rate
* **NumCompaniesWorked** - Number of companies worked at
* **Over18** - Over 18 years of age?
* **OverTime** - Overtime?
* **PercentSalaryHike** - The percentage increase in salary last year
* **PerformanceRating** - 1-Low, 2-Good, 3-Excellent, 4-Outstanding
* **RelationshipSatisfaction** - 1-Low, 2-Medium, 3-High, 4-Very High
* **StandardHours** - Standard Hours
* **StockOptionLevel** - Stock Option Level
* **TotalWorkingYears** - Total years worked
* **TrainingTimesLastYear** - Number of training attended last year
* **WorkLifeBalance** - 1-Low, 2-Good, 3-Excellent, 4-Outstanding
* **YearsAtCompany** - Years at Company
* **YearsInCurrentRole** - Years in the current role
* **YearsSinceLastPromotion** - Years since the last promotion
* **YearsWithCurrManager** - Years with the current manager

Setup environment:
1. Pengaturan Virtual Environtment
- Membuat dan mengaktifkan Env
    - Windows :
        ```
        python -m venv venv
        .\venv\Scripts\activate
        ```
    - Linux/MacOS: :
        ```
        python3 -m venv venv
        source venv/bin/activate
        ```
- Menginstal Dependensi<br>
    - Install menggunakan pip pada file requirements.txt
        ```
        pip install -r requirements.txt
        ```
- Jupyter Notebook
    - Install dan Menjalankan Jupyter 
        ```
        pip install jupyter
        jupyter notebook
        ```
- Menjalankan Model
    - Menjalankan model untuk prediksi
        ```
        python prediction.py
        ```

    - menyimpan hasil prediksi ke database PostgreSQL di superbase ke metabase
        ```
        python main.py
        ```
- Menjalankan Metabase dengan Docker
    - Pull docker image metabase
        ```
        docker pull metabase/metabase
        ```
    - Jalan metabase
        ```
        docker run -d -p 3000:3000 --name metabase metabase/metabase
        ```
        akan muncul : [Browser](http://localhost:3000)
- Menjalankan Stremlit

- Mengaktifkan dan Menonaktifkan Layanan dengan Docker
    - Menjalankan Docker Containers
        - Metabase : 
            ```
            docker start metabase
            ```
    - Menghentikan Docker Containers
        - Metabase : 
            ```
            docker stop metabase
            ```
    - Menghapus Docker Containers setelah selesai
        - Metabase : 
            ```
            docker rm metabase
            ```
    - Streamlit : 
        ```
        streamlit run main.py
        ```
## Business Dashboard

Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

![Dashboard](images/muazahaladawiyah-dashboard.png)

Dashboard yang dikembangkan mencakup:
- Distribusi karyawan keluar dan bertahan.
- Filter interaktif berdasarkan jabatan, departemen, dan usia.
- Visualisasi faktor-faktor signifikan seperti Monthly Income, Total Working Years, dan YearsAtCompany.

Link Dashboard (Metabase): [Dashboard Metabase](http://localhost:3000/public/dashboard/cc9a4959-3cbd-49e3-9911-12d19293964f)<br>
Link Aplikasi Prediksi (Streamlit): [Dashboard Streamlit](https://datascience1-scmjkwwehxnges9qsqcg7r.streamlit.app/)

## Conclusion

Jelaskan konklusi dari proyek yang dikerjakan.

Berdasarkan hasil eksplorasi data dan pemodelan yang telah dilakukan terhadap data karyawan PT Jaya Jaya Maju, dapat disimpulkan bahwa:
- Tingkat attrition (resign) karyawan di perusahaan cukup signifikan dan perlu perhatian khusus dari divisi HR.
- Berdasarkan analisis eksploratif (EDA), terdapat beberapa faktor yang paling berkontribusi terhadap tingginya risiko attrition, yaitu:
    - Pendapatan bulanan (Monthly Income),
    - Jarak rumah ke kantor (Distance From Home),
    - Jumlah perusahaan sebelumnya (NumCompaniesWorked),
    - Lama bekerja di perusahaan saat ini (YearsAtCompany),
    - dan Jumlah tahun bekerja secara total (TotalWorkingYears).
- Setelah melakukan training dan evaluasi pada lima model klasifikasi (Logistic Regression, Decision Tree, Random Forest, XGBoost, dan Neural Network/MLP), model Random Forest menunjukkan performa terbaik dengan hasil evaluasi di data uji sebagai berikut:
    - Accuracy: tinggi (misalnya, ~85.8%)
    - Precision dan Recall: seimbang, menunjukkan kemampuan model dalam mengenali karyawan yang berpotensi keluar cukup andal
    - F1-Score: konsisten tinggi, artinya model mampu menangani class imbalance dengan baik.
    
    Oleh karena itu, Random Forest dipilih sebagai model final untuk memprediksi kemungkinan karyawan akan keluar dari perusahaan (attrition prediction). Model ini kemudian digunakan untuk memprediksi data baru dan hasilnya diintegrasikan ke dalam dashboard monitoring HR.

### Rekomendasi Action Items (Optional)

Beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka yaitu :
1. Evaluasi dan Optimalkan Paket Kompensasi
    - Tingkatkan Penghasilan bagi karyawan dengan penghasilan rendah yang berisiko tinggi untuk resign, terutama pada mereka yang telah bekerja selama beberapa tahun dan memiliki pengalaman yang signifikan.
    - Mengidentifikasi faktor-faktor yang berhubungan dengan pemberian bonus atau insentif yang bisa meningkatkan loyalitas.

2. Perbaiki Work-Life Balance
    - Menyediakan kebijakan fleksibilitas jam kerja atau kerja jarak jauh untuk karyawan yang tinggal jauh dari kantor, guna mengurangi ketidaknyamanan dalam hal Distance From Home.
    - Menyediakan program wellness dan kesehatan mental untuk meningkatkan kepuasan kerja dan mengurangi stres yang mungkin berkontribusi pada keputusan untuk keluar.

3. Penyuluhan tentang Karier dan Peluang Kenaikan Jabatan
    - Meningkatkan program pelatihan dan pengembangan karier, dengan memberi kesempatan kepada karyawan untuk mengembangkan keterampilan dan membangun jalur karier jangka panjang.
    - Menawarkan program rotasi jabatan untuk mereka yang merasa stagnan setelah bekerja beberapa tahun (misalnya YearsAtCompany).

4. Pendekatan Proaktif pada Karyawan Baru
    - Fokus pada onboarding program yang lebih efektif untuk karyawan baru guna meminimalkan turnover dalam beberapa bulan pertama.
    - Memperkenalkan karyawan baru dengan mentorship dari karyawan senior untuk mempercepat integrasi mereka ke dalam budaya perusahaan.

5. Peningkatan Kepuasan Kerja
    - Berdasarkan faktor-faktor yang berhubungan dengan JobSatisfaction dan JobInvolvement, perusahaan dapat mengidentifikasi area di mana kebijakan atau fasilitas perlu ditingkatkan.
    - Meningkatkan komunikasi antara manajer dan tim untuk memastikan karyawan merasa dihargai dan memiliki peluang untuk memberikan umpan balik.

6. Gunakan dashboard sebagai alat monitoring berkala oleh divisi HR dan manajemen.

Dengan mengimplementasikan action items ini, perusahaan dapat memitigasi faktor-faktor yang mempengaruhi keputusan resign, serta menciptakan lingkungan kerja yang lebih menarik bagi karyawan yang ada dan potensi karyawan yang baru.