"""Membuat WEB Lowongan Kerja"""
from flask import Flask,render_template

app = Flask(__name__)

def datalowongan ():
    """data lowongan yang akan tampil"""
    return [
        {
            'title': 'Sales Manager',
            'company': 'PT Tigaraksa Satria',
            'location': 'Kalimatan Tengan',
            'description': 'Membutuhkan karyawan yang expert di bidangnya',
            'link': 'https://id.jobstreet.com/id/job/79863569?ref=search-standalone&origin=showNewTab#sol=de314323e8b215952e83d80404fa9d76deb0d8a1'
        },
        {
            'title': 'Web Developer',
            'company': 'FinShot',
            'location': 'Jakarta',
            'description': 'Pengembangan dan Produksi WEB',
            'link': 'https://id.jobstreet.com/id/job/79881492?ref=search-standalone&origin=jobTitle#sol=b102ddcfb4691cb6d11106b0b92aa30e3fafd2aa'
        },
        {
            'title': 'Kepala Keungan',
            'company': 'PT Tomypak Makmur',
            'location': 'Jakarta Barat',
            'description': 'Membutuhkan Accounting Section Head',
            'link': 'https://www.loker.id/akuntansi-keuangan/manajemen-akuntansi/section-head-accounting-finance-pt-tomypak-makmur-jakarta-barat.html'
        },
        {
            'title': 'Asisten Sipil',
            'company': 'Gozco Plantations',
            'location': 'Palembang',
            'description': 'Membutuh staf asisten sipil untuk membantu dalam membuat dan menganalisa rencan kerja di palembang',
            'link': 'https://www.loker.id/teknik/sipil/asisten-sipil-gozco-plantations-palembang.html'
        },
        {
            'title': 'Ice Cream Scooper',
            'company': 'Honest Spoon',
            'location': 'Tangerang Selatan',
            'description': 'Mencari pegawai yang memiliki etos kerja tinggi',
            'link': 'https://www.loker.id/ritel/asisten-ritel/ice-cream-scooper-honest-spoon-tangerang-selatan.html'
        },
        {
            'title': 'Manager Kebun',
            'company': 'Indo Karya Group',
            'location': 'Kalimantan Barat',
            'description': 'Mencari pegawai yang memiliki etos kerja tinggi',
            'link': 'https://www.loker.id/ritel/asisten-ritel/ice-cream-scooper-honest-spoon-tangerang-selatan.html'
        },
        {
            'title': 'Kurir Motor',
            'company': 'PT Wahana Express Semarang',
            'location': 'Semarang',
            'description': 'Membutuhkan pegawai yang berdomisili asli Semarang',
            'link': 'https://pintarnya.com/kerja/lowongan/kurir-motor-417924'
        },
        {
            'title': 'Supervisor Operasional Kapal',
            'company': 'PT Pelayaran Pasifik Indonesia',
            'location': 'Jakarta Barat',
            'description': 'Manajemen Armada (Manufaktur, Transportasim & Logistik)',
            'link': 'https://pintarnya.com/kerja/lowongan/kurir-motor-417924'
        },
        {
            'title': 'Operator Mesin dan Las (Perkapalan)',
            'company': 'PT Indo Shipping Operator',
            'location': 'Banten',
            'description': 'Dibutuhkan mesin dan las berpengalaman',
            'link': 'https://id.jobstreet.com/id/job/79962459?ref=search-standalone&origin=jobTitle#sol=e1d97365d1bca012f573ec4bfd0134d2468f8f19'
        },
        {
            'title': 'Pelaksana Lapangan',
            'company': 'JHP contractor',
            'location': 'Surabaya',
            'description': 'JHP Contractor membutuhkan tenaga kerja sebagai pelaksana lapangan (Untuk proyek)',
            'link': 'https://www.loker.id/konstruksi-dan-bangunan/site-supervisor/pelaksana-lapangan-jhp-contractor-surabaya.html'
        }
    ]

@app.route ('/')
def home ():
    """Render Home"""
    return render_template ('home.html')

@app.route ('/jobs')
def job ():
    """Render Job"""
    job_listings = datalowongan ()
    return render_template ('job.html', jobs=job_listings)

@app.route ('/about')
def about ():
    """Render About"""
    return render_template ('about.html')

if __name__ == ('__main__'):
    app.run (host='0.0.0.0',port = '80' ,debug=True)
