import ipaddress
import tkinter as tk
from tkinter import filedialog, Toplevel, ttk

# Global değişkeni tanımla
ip_version = "IPv4"  # Varsayılan olarak IPv4 seçilir

def ip_subnet_calculator(ip_address, subnet_mask, result_label=None, version="IPv4"):
    try:
        if version == "IPv4":
            network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
        else:
            network = ipaddress.IPv6Network(f"{ip_address}/{subnet_mask}", strict=False)

        result = {
            f'{version} Adresi': ip_address,
            'Ağ Adresi': str(network.network_address),
            'Kullanılabilir Host IP Aralığı': f"{str(network.network_address + 1)} - {str(network.network_address + network.num_addresses - 2)}",
            'Yayın Adresi': str(network.broadcast_address),
            'Toplam Host Sayısı': network.num_addresses,
            'Kullanılabilir Host Sayısı': network.num_addresses - 2,
            'Subnet Maskesi': str(network.netmask),
            'Wildcard Maskesi': str(network.hostmask),
            'İkili Subnet Maskesi': '.'.join([bin(int(x))[2:].zfill(8) for x in str(network.netmask).split('.')]),
            'CIDR Notasyonu': f"/{network.prefixlen}",
            'IP Türü': 'Halka Açık' if not network.is_private else 'Özel',
            'İkili ID': format(int(ipaddress.IPv4Address(ip_address)), '032b') if version == "IPv4" else format(int(ipaddress.IPv6Address(ip_address)), '128b'),
            'Tam Sayı ID': int(ipaddress.IPv4Address(ip_address)) if version == "IPv4" else int(ipaddress.IPv6Address(ip_address)),
            'Hex ID': hex(int(ipaddress.IPv4Address(ip_address))) if version == "IPv4" else hex(int(ipaddress.IPv6Address(ip_address))),
            'in-addr.arpa': '.'.join(reversed(ip_address.split('.'))) + '.in-addr.arpa' if version == "IPv4" else f"{ip_address}.ip6.arpa",
            'IPv4 Mapped Adresi': f"::ffff:{hex(int(ipaddress.IPv4Address(ip_address)))[2:]}" if version == "IPv4" else "N/A",
            '6to4 Öneki': f"2002:{hex(int(ipaddress.IPv4Address(ip_address)))[2:]}::/48" if version == "IPv4" else "N/A"
        }

        if result_label:
            result_text = "\n".join([f"{key}: {value}" for key, value in result.items()])
            result_label.config(text=result_text, fg="green")  # Sonuç yazılarının rengi yeşil
        else:
            print("\n".join([f"{key}: {value}" for key, value in result.items()]))
        return result_text  # Çıktıyı döndür

    except ValueError as e:
        if result_label:
            result_label.config(text=f"Hata: {e}", fg="red")  # Hata yazılarının rengi kırmızı
        else:
            print(f"Hata: {e}")

def save_to_file(result_text):
    # Dosya kaydetme penceresi
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(result_text)

def show_example_table():
    # Yeni pencere oluştur
    table_window = Toplevel()
    table_window.title("Örnek Subnet Tablosu")

    # Pencere boyutları
    window_width = 800  # Genişlik
    window_height = 300  # Yükseklik artırıldı
    screen_width = table_window.winfo_screenwidth()
    screen_height = table_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    table_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    # Tabloyu yerleştirmek için bir çerçeve oluştur
    frame = tk.Frame(table_window)
    frame.pack(padx=10, pady=10)

    # Tablo başlıkları
    columns = ("Prefix Size", "Network Mask", "Usable Hosts per Subnet")
    tree = ttk.Treeview(frame, columns=columns, show="headings")

    # Sütun genişlikleri
    tree.column("Prefix Size", width=150)  # Prefix Size sütunu genişliği
    tree.column("Network Mask", width=300)  # Network Mask sütunu genişliği
    tree.column("Usable Hosts per Subnet", width=300)  # Usable Hosts per Subnet sütunu genişliği

    # Yüksekliği artırmak için bir scrollbar ekleyelim
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side='right', fill='y')
    tree.pack(padx=10, pady=10, fill='both', expand=True)

    # Başlıklar
    for col in columns:
        tree.heading(col, text=col)

    # Tablo verilerini ekle
    table_data = [
        # Class A
        ("Class A", "", "", ""),
        ("/1", "128.0.0.0", "2,147,483,646", "Class A"),
        ("/2", "192.0.0.0", "1,073,741,822", "Class A"),
        ("/3", "224.0.0.0", "536,870,910", "Class A"),
        ("/4", "240.0.0.0", "268,435,454", "Class A"),
        ("/5", "248.0.0.0", "134,217,726", "Class A"),
        ("/6", "252.0.0.0", "67,108,862", "Class A"),
        ("/7", "254.0.0.0", "33,554,430", "Class A"),
        ("/8", "255.0.0.0", "16,777,214", "Class A"),

        # Class B
        ("Class B", "", "", ""),
        ("/9", "255.128.0.0", "8,388,606", "Class B"),
        ("/10", "255.192.0.0", "4,194,302", "Class B"),
        ("/11", "255.224.0.0", "2,097,150", "Class B"),
        ("/12", "255.240.0.0", "1,048,574", "Class B"),
        ("/13", "255.248.0.0", "524,286", "Class B"),
        ("/14", "255.252.0.0", "262,142", "Class B"),
        ("/15", "255.254.0.0", "131,070", "Class B"),
        ("/16", "255.255.0.0", "65,534", "Class B"),

        # Class C
        ("Class C", "", "", ""),
        ("/17", "255.255.128.0", "32,766", "Class C"),
        ("/18", "255.255.192.0", "16,382", "Class C"),
        ("/19", "255.255.224.0", "8,190", "Class C"),
        ("/20", "255.255.240.0", "4,094", "Class C"),
        ("/21", "255.255.248.0", "2,046", "Class C"),
        ("/22", "255.255.252.0", "1,022", "Class C"),
        ("/23", "255.255.254.0", "510", "Class C"),
        ("/24", "255.255.255.0", "254", "Class C"),
        ("/25", "255.255.255.128", "126", "Class C"),
        ("/26", "255.255.255.192", "62", "Class C"),
        ("/27", "255.255.255.224", "30", "Class C"),
        ("/28", "255.255.255.240", "14", "Class C"),
        ("/29", "255.255.255.248", "6", "Class C"),
        ("/30", "255.255.255.252", "2", "Class C" ),
        ("/31", "255.255.255.254", "0", "Class C"),
        ("/32", "255.255.255.255", "0", "Class C")
    ]

    for row in table_data:
        tree.insert("", tk.END, values=row)

def show_explanations():
    # Yeni pencere oluştur
    explanation_window = Toplevel()
    explanation_window.title("Açıklamalar")

    # Pencere boyutları
    window_width = 1100
    window_height = 500
    screen_width = explanation_window.winfo_screenwidth()
    screen_height = explanation_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    explanation_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    # Canvas ve scrollbar ekle
    canvas = tk.Canvas(explanation_window)
    scrollbar = ttk.Scrollbar(explanation_window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Frame'i canvas içine yerleştir
    canvas_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

    # Açıklama metinlerini ekleyelim
    explanations = {
    "IP Adresi": """
        IP (Internet Protocol) adresi, bir ağda her cihazın tanımlanabilmesi için kullanılan benzersiz bir sayısal etikettir.
        Bir IP adresi, cihazların birbirleriyle iletişim kurmasını sağlar. İnternete bağlı her cihazın bir IP adresi vardır.
        IPv4'te bu adresler 32-bit'lik sayılardır ve genellikle 4 oktet (byte) şeklinde ifade edilir (örneğin, 192.168.1.1).
        IPv6 ise 128-bit'lik adresleme kullanır ve daha geniş bir adres aralığı sağlar. IPv6 adresleri, sekiz grup 16-bit'lik
        hexadecimal sayıdan oluşur (örneğin, 2001:0db8:85a3:0000:0000:8a2e:0370:7334).
    """,
    "Subnet Maskesi": """
        Subnet maskesi, bir IP ağını daha küçük alt ağlara bölen bir parametredir. Subnet maskesi, IP adresiyle birlikte 
        ağın hangi kısmının cihaz (host) ve hangi kısmının ağ (network) olduğunu belirler.
        Subnet maskesi, IP adresindeki ağ kısmını tanımlamak için kullanılır. Örneğin, 255.255.255.0 maskesi, ağın 
        ilk üç oktetinin ağ kısmını, son oktetinin ise host kısmını belirlediğini ifade eder.
        Bu, ağdaki cihazların birbiriyle iletişim kurabilmesi için önemlidir. Subnet maskesiyle birlikte ağ adresi 
        ve yayın adresi gibi kavramlar da belirlenir.
    """,
    "Ağ Adresi": """
        Ağ adresi, bir IP adresinin ağ kısmını temsil eden ve ağın kimliğini belirleyen özel bir IP adresidir.
        Ağ adresi, ağdaki cihazların birbirleriyle iletişim kurabilmesi için kullanılır. IP adreslerinin alt ağlara 
        bölünmesinden sonra, bu adres ağın "kimliğini" temsil eder ve genellikle cihazlar tarafından yönlendirici 
        (router) üzerinden ağ dışındaki cihazlarla iletişim kurmada kullanılır.
        Örneğin, 192.168.1.0 ağ adresi, 192.168.1.1'den 192.168.1.254'e kadar olan cihazların bu ağda olduğunu 
        belirtir. Ağ adresinin sonundaki bitler sıfırdır.
    """,
    "Yayın Adresi": """
        Yayın adresi (broadcast address), aynı ağdaki tüm cihazlara bir mesaj göndermek için kullanılan özel 
        bir IP adresidir. Bir ağdaki tüm cihazlar, yayın adresi üzerinden gönderilen verileri alır.
        Yayın adresi, ağın son IP adresidir ve tüm host kısmı 1 olarak ayarlanır. Örneğin, 192.168.1.255, 
        192.168.1.0/24 ağındaki yayın adresidir. Bu adres, ağdaki tüm cihazların alacağı bir yayını temsil eder.
        Yani, bir cihaz yayın adresine mesaj gönderdiğinde, ağdaki diğer tüm cihazlar bu mesajı alır.
    """,
    "Kullanılabilir Host Sayısı": """
        Kullanılabilir host sayısı, bir ağdaki IP adreslerinden sadece ağ adresi ve yayın adresi hariç kalan 
        cihazlara tahsis edilebilen IP adresleri sayısını belirtir. Ağ adresi ve yayın adresi, hostlar tarafından 
        kullanılamaz çünkü bu adresler ağdaki yönlendirme ve iletişim için rezerve edilmiştir.
        Örneğin, 192.168.1.0/24 ağında, ağ adresi 192.168.1.0 ve yayın adresi 192.168.1.255 olduğu için,
        192.168.1.1'den 192.168.1.254'e kadar olan 254 adres hostlar için kullanılabilir.
    """,
    "CIDR Notasyonu": """
        CIDR (Classless Inter-Domain Routing) notasyonu, IP adresinin bit uzunluğunu belirtmek için kullanılan
        bir yöntemdir. CIDR, IP adresinin sonundaki bir slash ("/") ve ardından gelen rakamla belirtilir, bu sayı
        ağın maskesinin (prefix) bit uzunluğunu ifade eder. CIDR notasyonu, ağın ne kadar büyük olduğunu belirtir.
        Örneğin, 192.168.1.0/24 adresi, 24 bitlik bir ağ maskesini gösterir ve bu ağda 256 adres bulunur.
        CIDR notasyonu, IP adresi sınıflandırmalarını (A, B, C) aşarak daha esnek ve verimli bir IP adresi 
        tahsisi sağlar.
    """,
    "Wildcard Maskesi": """
        Wildcard maskesi, subnet maskesinin tersidir ve ağda hangi bitlerin değiştirilebileceğini gösterir. 
        Subnet maskesi, ağ kısmı ile host kısmını ayırırken, wildcard maskesi hangi bitlerin değiştirilebileceği 
        hakkında bilgi verir.
        Wildcard maskesi genellikle yönlendirme tablolarında (routing tables) kullanılır. Wildcard maskesi, 
        subnet maskesinin her oktetindeki 1'leri 0'a, 0'ları ise 1'e dönüştürür. Örneğin, subnet maskesi 255.255.255.0 
        ise wildcard maskesi 0.0.0.255 olur. Bu, ağın son kısmındaki (host kısmındaki) adreslerin değiştirilebileceğini belirtir.
    """
}

    # Her başlık ve açıklama için bir etiket ekleyelim
    for idx, (title, explanation) in enumerate(explanations.items()):
        label_title = tk.Label(canvas_frame, text=title, font=("Helvetica", 12, "bold"))
        label_title.pack(pady=5)
        
        label_explanation = tk.Label(canvas_frame, text=explanation, font=("Helvetica", 10))
        label_explanation.pack(padx=10, pady=5)

    # Canvas frame boyutlarını ayarla
    canvas_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


def gui_mode():
    root = tk.Tk()
    root.title("IP Subnet Hesaplayıcı")

    window_width = 900
    window_height = 900
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    title_label = tk.Label(
        root, 
        text="IP Subnet Hesaplayıcı", 
        font=("Helvetica", 30, "bold"),
        fg="red",  # Başlık yazılarının rengi kırmızı
        bg="lightyellow",
        relief="solid",
        padx=20, pady=20
    )
    title_label.pack(pady=10)

    # AÇIKLAMALAR Butonu
    explanation_button = tk.Button(root, text="AÇIKLAMALAR", command=show_explanations, bg="lightblue")
    explanation_button.pack(pady=10)

    # Yeni Hesaplama Butonu
    def new_calculation():
        ip_entry.delete(0, tk.END)
        subnet_entry.delete(0, tk.END)
        result_label.config(text="")

        # IP sürümü butonlarını tekrar görünür hale getirme
        ipv4_button.pack(pady=10)
        ipv6_button.pack(pady=10)

        # Hesaplama butonlarını gizleme
        ip_entry_label.pack_forget()
        ip_entry.pack_forget()
        subnet_entry_label.pack_forget()
        subnet_entry.pack_forget()
        calculate_button.pack_forget()
        button_frame.pack_forget()  # Buton çerçevesini gizle

    # Hesaplama işlemi
    def calculate():
        ip_address = ip_entry.get()
        subnet_mask = subnet_entry.get()
        version = ip_version
        if ip_address and subnet_mask:
            result_text = ip_subnet_calculator(ip_address, subnet_mask, result_label, version)
            save_button.pack(pady=10)  # Çıktı yazdır butonunu göster
        else:
            result_label.config(text="Lütfen hem IP adresi hem de subnet maskesi girin.", fg="red")

    # IP sürümünü seçme
    def choose_ip_version(version):
        global ip_version
        ip_version = version
        
        # IP ve subnet maskesi giriş alanlarını gösterme
        ipv4_button.pack_forget()
        ipv6_button.pack_forget()

        ip_entry_label.pack(pady=5)
        ip_entry.pack(pady=5)
        subnet_entry_label.pack(pady=5)
        subnet_entry.pack(pady=5)
        calculate_button.pack(pady=10)

        # Buton çerçevesini göster
        button_frame.pack(pady=10)

        # IP etiketlerini sürüme göre ayarla
        if version == "IPv4":
            ip_entry_label.config(text="IP Adresini Girin (örn: 192.168.1.1):")
            subnet_entry_label.config(text="Subnet Maskesini Girin (örn: 255.255.255.0):")
        else:
            ip_entry_label.config(text="IPv6 Adresini Girin (örn: 2001:0db8:85a3:0000:0000:8a2e:0370:7334):")
            subnet_entry_label.config(text="IPv6 Subnet Maskesini Girin (örn: ffff:ffff:ffff:ffff::):")


    # Başlangıç ekranında IPv4 veya IPv6 seçimi yapma
    ipv4_button = tk.Button(root, text="IPv4 Hesaplama", command=lambda: choose_ip_version("IPv4"), bg="lightgreen")
    ipv4_button.pack(pady=10)

    ipv6_button = tk.Button(root, text="IPv6 Hesaplama", command=lambda: choose_ip_version("IPv6"), bg="lightgreen")
    ipv6_button.pack(pady=10)

    # IP Adresi için Etiket ve Giriş (Başlangıçta gizli)
    ip_entry_label = tk.Label(root, text="IP Adresini Girin (örn: 123.123.123.123):")
    ip_entry = tk.Entry(root)

    # Subnet Maskesi için Etiket ve Giriş (Başlangıçta gizli)
    subnet_entry_label = tk.Label(root, text="Subnet Maskesini Girin (örn: 255.255.255.252):")
    subnet_entry = tk.Entry(root)

    # Sonuçları Gösterme Etiketi
    result_label = tk.Label(root, text="", font=("Courier", 10), justify="left", anchor="nw")
    result_label.pack(pady=10)

    # Hesapla Butonu
    calculate_button = tk.Button(root, text="Hesapla", command=calculate, bg="lightcoral")

    # Butonlar için çerçeve
    button_frame = tk.Frame(root)

    # Yeni Hesaplama Butonu
    new_button = tk.Button(button_frame, text="Yeni", command=new_calculation, bg="lightgreen")
    new_button.pack(side=tk.LEFT, padx=5)

    # Kapat Butonu
    close_button = tk.Button(button_frame, text="Kapat", command=root.quit, bg="lightgrey")
    close_button .pack(side=tk.LEFT, padx=5)

    # Çıktı Yazdır Butonu
    save_button = tk.Button(button_frame, text="Çıktı Yazdır", command=lambda: save_to_file(result_label.cget("text")), bg="lightblue")
    save_button.pack(side=tk.LEFT, padx=5)

    # Buton çerçevesini gizle
    button_frame.pack_forget()

    # Örnek Tabloyu Göster Butonu
    example_table_button = tk.Button(root, text="Örnek Subnet Tablosu", command=show_example_table, bg="lightyellow")
    example_table_button.pack(pady=4)

    # Butonların hover (fareyle üzerine gelme) renk değiştirmesi
    def on_hover(event):
        event.widget.config(bg="gray")

    def off_hover(event, color):
        event.widget.config(bg=color)

    for button in [ipv4_button, ipv6_button, calculate_button, save_button, new_button, close_button, example_table_button]:
        button.bind("<Enter>", on_hover)
        button.bind("<Leave>", lambda event, color=button.cget('bg'): off_hover(event, color))

    root.mainloop()

# GUI'yi başlat
gui_mode()
