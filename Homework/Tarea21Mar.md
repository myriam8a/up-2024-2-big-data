
Tarea SQL 21 Marzo
=============

_By Myriam Ochoa_


Excercise 1
------------

### Show the most expensive products from each brand

    SELECT m.title as Manufacturer, max(a.price) as MaxPrice, max(a.title) as Categories
    FROM articles AS a
    JOIN manufacturers AS m ON a.manufacturer_id = m.id
    GROUP BY m.title
    ORDER BY max(a.price) DESC;

First three columns from two different tables are selected. The m.title represents the manufacturer's name, aliased as "Manufacturer". The max(a.price) gives the highest price of the manufacturer's articles, aliased as "MaxPrice". The max(a.title) is intended to fetch a value from the article titles, aliased as "Categories"

Then, two tables are joined; articles (aliased as a) and manufacturers (aliased as m), using the manufacturer_id field in the articles table and the id field in the manufacturers table. The join ensures that only those rows with matching IDs in both tables are selected.  The **Group By** groups the results by the manufacturer's title. 

Finally, the results are ordered based on the maximum price of the articles for each manufacturer.

**Results:**

| Manufacturer | MaxPrice | Categories |
| :--- | :--- | :--- |
| HP ENTERPRISE | 179669 | Servidor HPE ProLiant MicroServer Gen10+, Intel Xeon E-2224 3.40GHz, 16GB DDR4, 1TB, máx. 16TB, 3.5", SATA, Ultra Micro Tower - no Sistema Operativo Instalado |
| DELL | 128829 | Servidor Dell PowerEdge R550, Intel Xeon Gold 5318Y 2.10GHz, 32GB DDR4, 480GB, 2.5", SATA III, Rack \(2U\) - no Sistema Operativo Instalado |
| HP | 93739 | Scanner HP ScanJet Pro 2600 f1, 600 x 600DPI, Escáner Color, Escaneado Dúplex, USB 2.0, Blanco |
| MSI | 93139 | MSI Tarjeta PCI Theater 550 Pro, 256MB, MPEG |
| APPLE | 87519 | Apple Watch Ultra GPS + Cellular, Caja de Titanio de 49mm, Correa Ocean Deportiva Grande Color Amarillo |
| TOUGHBOOK PANASONIC | 85939 | Laptop Panasonic Toughbook FZ-55DZ03MTM 14" HD, Intel Core i5-1145G7 2.60GHz, 16GB, 512GB SSD, Windows 10 Pro 64-bit, Español, Negro |
| ASUS | 82319 | Mousepad ASUS NC12 TUF GAMING P1 DS, 36 x 26cm, Grosor 3mm, Demon Slayer L.E. Nezuko Kamado |
| LENOVO | 80209 | Tablet Lenovo Tab M10 Gen 3 10.1", 4G LTE, 32GB, Android 11, Gris |
| VSSL | 60989 | VSSL Extensor de Audio A.6X, 6 Zonas, 12 x 50W, Wi-Fi, Bluetooth, con Chromecast y Google Assistant |
| ALIENWARE | 59069 | Laptop Gamer Alienware X17 R2 17.3" Full HD, Intel Core i7-12700H 2.30GHz, 16GB, 512GB SSD, NVIDIA GeForce RTX 3060, Windows 11 Home 64-bit, Español, Blanco |
| DKS DOORKING | 51689 | DKS Doorking Barrera Vehicular 1601-380, hasta 4 Metros - no Incluye Mástil |
| GIGABYTE | 48949 | Tarjeta Madre Gigabyte Micro ATX B560M DS3H V2, S-1200, Intel B560 Express, HDMI, 128GB DDR4 para Intel |
| ELO TOUCHSYSTEMS | 43659 | Elo TouchSystems Sistema POS E484291 17”, Intel Core i3-8100T 3.10GHz, 4GB, 128GB SSD,  Windows 10 Home |
| SAMSUNG | 38889 | Samsung Flip 2.0 Pantalla Comercial LCD Touch 55", Blanco - no Incluye Base |
| ACER | 38309 | Laptop Gamer Acer Nitro AN515-45-R6XD 15.6" Full HD, AMD Ryzen 5 5600H 3.30GHz, 8GB, 512GB SSD, NVIDIA GeForce RTX 3060, Windows 11 Home 64-bit, Español, Negro |
| PNY | 36849 | Tarjeta de Video PNY NVIDIA GeForce RTX 4090 24GB OC XLR8 Gaming Verto EPIC-X RGB TF, 24GB 384-bit GDDR6X, PCI Express x16 4.0 |
| EVOLIS | 35539 | Evolis PM2-0025-A Impresora de Tarjetas, Transferencia Térmica, 300 x 1200 DPI, USB, Ethernet, Negro/Blanco |
| ONKYO | 35009 | Onkyo Receptor AV TX-NR7100 para Home Cinema, 7.2 Canales, Certificado THX, IMAX Enhanced, Dolby Atmos/DTS:X, 8K, HDMI 2.1, Wi-Fi, Bluetooth, Negro, Compatible con Alexa/Google Assistant/Apple Airplay |
| AORUS | 32939 | Laptop Gamer AORUS 5 SE4 15.6" Full HD, Intel Core i7-12700H 3.50GHz, 16GB, 512GB SSD, NVIDIA GeForce RTX 3070, Windows 11 Home 64-bit, Español, Negro |
| XPG | 30399 | XPG Tiras LED con Control Prime ARGB, 60cm x 10mm, Negro |
| BROTHER | 27569 | Tóner Brother TN-750 Negro, 8000 Páginas |
| HUAWEI | 27539 | Laptop Huawei MateBook D16 16.1" Full HD, AMD Ryzen 5 4600H 3GHz, 16GB, 512GB SSD, Windows 10 Home 64-bit, Español, Gris |
| EPSON | 26719 | Tanque de Tinta Epson T673, 70ml, 6 Piezas |
| CISCO | 25039 | Cisco Módulo FlexStack-Plus para Switch Catalyst 2960-X |
| StarTech.com | 22829 | StarTech.com Tapete Antiestatico de PVC, 60x70cm, Beige |
| UBIQUITI NETWORKS | 22719 | Ubiquiti Networks Terminal de Línea Óptica UFiber OLT4, 4x PON, 1x SFP |
| CYBERPOWER | 21709 | CyberPower Transformador Reductor OL5KSTF, Entrada 208V, Salida 120V |
| DYNABOOK | 20989 | Laptop Dynabook Tecra A40-J 14" Full HD, Intel Core i5-1135G7 2.40GHz, 8GB, 512GB SSD, Windows 10 Pro 64-bit, Español, Azul ― incluye 3 Años de Garantía en Sitio |
| BENQ | 20679 | BenQ Kit Adaptador Inalámbrico para Proyector InstaShow WDC10, HDMI, Negro |
| HONOR | 19579 | Laptop Honor MagicBook 15 15.6" Full HD, AMD Ryzen 5 3500U 2.10GHz, 16GB, 512GB SSD, Windows 10 Home 64-bit, Inglés, Gris Mate |
| GRIZZLY | 18629 | Computadora Gamer Grizzly Draknosh, AMD Ryzen 7 Pro 4750G 3.60GHz, 16GB, 1TB + 500GB SSD, NVIDIA GeForce RTX 3060, Windows 10 Prueba |
| WEBOOST | 17879 | Weboost Kit de Amplificador de Señal Celular, 3G/4G, 700MHz, 70dB, 3000² Metros |
| LANIX | 16249 | Laptop Lanix Neuron X Pro 41298 14" Full HD, Intel Core i5-1135G7 2.40GHz, 8GB, 512GB SSD, Windows 10 64-bit, Español, Negro |
| URREA | 15999 | Urrea Torquímetro de Carátula 6119, Cuadro 3/8", 40.6cm, Aluminio |
| PROVISION ISR | 15729 | Provision-ISR Servidor de Video OC-MSCL-S\(DT\)-V2, 256 Canales, 1x HDMI, 4K, 1x RJ-45 |
| XEROX | 15679 | Xerox Módulo Realizador de Folletos 497K20590, para AltaLink C81XX/B81XX ― Requiere EZK para su Correcto Funcionamiento, se Vende por Separado |
| ACCESSPRO | 15119 | AccessPro Torniquete Bidireccional AP5000HD, 98cm, Acero Inoxidable |
| DATAPRODUCTS | 14969 | DataProducts Impresora 2600, Blanco y Negro, Matriz de Puntos, 360 x 360 DPI, USB, Negro |
| HIKMICRO | 14509 | Hikmicro Cámara Térmica Portátil Pocket 2 3.5", 4x Zoom, WiFi, Negro |
| MICROSOFT | 14379 | Xbox Live Gold, 1 Año ― Producto Digital Descargable |
| SONY | 14199 | Sony PlayStation 5 Digital Edition 825GB, WiFi, Bluetooth 5.1, Blanco/Negro ― Incluye Juego Horizon Forbidden West |
| ZEBRA | 13979 | Zebra Tarjetas de PVC para Credenciales Premier, 2.12" x 3.38", 500 Tarjetas, para Impresoras Zebra |
| WHIRLPOOL | 13959 | Whirlpool Refrigerador WT1870A, 18 Pies Cúbicos, Plata |
| HONEYWELL | 12879 | Honeywell Terminal Portátil EDA71 7", 2GB, Android, Bluetooth |
| LG | 12369 | LG Smart TV LED UHD AI ThinQ UQ80 55", 4K Ultra HD, Negro |
| CANON | 11459 | Canon Kit Cabezal para Pixma G1100/G2100/G3100/G4100 |
| MEGALUZ | 10609 | Proyector de Luz Contour 30, 1 Pieza |
| DAHUA | 10429 | Dahua Panel de Alarma ARC3000H-W2, hasta 150 Dispositivos, Inalámbrico |
| EPCOM | 10319 | Epcom Soporte para Amplificadores, Gris |
| VORAGO | 10239 | Vorago Soporte de Pared TM-300 para Pantalla 13" - 42", hasta 25kg, Negro |
| LINKSYS | 9669 | Router Linksys con Sistema de Red Wi-Fi en Malla MX10600, 2402Mbps, 2.4/5/5GHz,  Antena Interna - 2 Piezas ― ¡Compre más de $1,999 en productos Linksys y participe en el sorteo de 1 Router WHW0101! |
| JABRA | 9419 | Jabra Sistema de Videoconferencia PanaCast, 4K Ultra HD 180°, 1x USB-C, Negro |
| GATEWAY | 9419 | Laptop Gateway Ultra Slim 14.1" Full HD, Intel Core i3-1005G1 1.20GHz, 4GB, 128GB SSD, Windows 10 Home S 64-bit, Inglés, Negro |
| SOLAX | 9329 | SolaX Inversor para Interconexión Grid-Tie X1-1.1-S-D, 1100W, 450V |
| GHIA | 9159 | Regulador Ghia GVR-010, 400W, 1000VA, Entrada 120V, Salida 120V, 4 Contactos |
| HIKVISION | 8489 | Hikvision Montaje para Sensor PIR DS-PDB-IN-U, Blanco |
| TOTAL GROUND | 8369 | Total Ground Kit de Tierra Física TG45AB, 45A - incluye Electrodo/H2Ohm/Registro |
| HYUNDAI | 8319 | Laptop Hyundai Thinnote-A 14.1" HD, Intel Celeron N3350 1.10GHz, 4GB, 64GB HDD, Windows 10 Pro 64-Bit, Inglés, Gris |
| TACX | 8299 | Tacx Kit Rodillos Entrenadores de Ciclismo Inteligentes Boost, ANT+, Bluetooth, Azul/Negro - Incluye Soporte y Cierre Rápido |
| BEA | 8159 | Bea Sensor de Microondas 10FALCON, Ángulo de 0 - 180° |
| SHURE | 7889 | Shure Kit Micrófonos para Bombos PGADRUMKIT5, Alámbrico, Negro |
| BIRD TECHNOLOGIES | 7869 | Bird Technologies Wattmetro 4230-006-1, Gris |
| RHEEM | 7399 | Rheem Calentador de Agua 89V40, Eléctrico 220V, 152 Litros/Hora, Gris |
| NINTENDO | 7309 | Nintendo Switch OLED, 64GB, Wi-Fi, Neón |
| ALLIED TELESIS | 7229 | Allied Telesis Módulo Transceptor MiniGbic AT-SPLX10A SFP, LC Monomodo, 1000 Mbit/s, 10Km, 1310nm |
| GARMIN | 6999 | Garmin Navegador GPS eTrex 32x, 2.2", USB, Negro/Gris |
| ALIEN | 6959 | Alien Luces LED Blanco, 5 Metros - incluye 1 Cable de Energía |
| ELGATO | 6719 | Elgato Tarjeta de Captura de Video Digital Cam Link Pro, 4K, 4x HDMI, PCIe |
| ZKTECO | 6379 | ZKTeco Unidad de Respaldo de Energía para Lectores Biométricos, 12V |
| SURTEK | 6319 | Surtek Polipasto POLPAL2, 1500Kg, Cadena 1.5 Metros, Amarillo |
| QIAN | 6039 | Teclado POS Qian QPA1702, Alámbrico, PS/2, Negro \(Español\) |
| FELLOWES | 5859 | Fellowes Trituradora de Corte Cruzado Powershred 12C, 12 Hojas, 19 Litros, Negro |
| BINDEN | 5849 | Drone Binden B19 con Cámara 4K, 4 Rotores, hasta 600 Metros, Blanco |
| POSLINE | 5789 | POSline Papel Térmico 45mm x 57mm, 50 Rollos |
| HISENSE | 5449 | Hisense Congelador FC50D6AWX1, 142L, 5 Pies Cúbicos, Blanco |
| PANASONIC | 5409 | Panasonic Teléfono IP con Pantalla LCD 4.3" KX-NT680X, Altavoz, Blanco |
| LINKEDPRO | 5399 | LinkedPRO Rack Abierto de 4 Postes 19", 45U, hasta 900kg, Negro |
| SEAGATE | 5209 | Disco Duro para NAS Seagate IronWolf Pro 3.5" de 1 a 24 Bahías, 10TB, SATA III, 6Gbit/s, 7200RPM, 256MB Caché |
| THOMSON | 5179 | Laptop Thomson WWN15i5-4BK256 15.6" Full HD, Intel Core i5-5257U 2.70GHz, 4GB, 256GB SSD, Windows 10 Home 64-bit, Inglés, Negro |
| ABB | 4869 | ABB Relevador de Apertura con Cableado, 240V, para T4/T5/T6 |
| LOGITECH | 4549 | Mouse Logitech Óptico Pebble M350, Inalámbrico, Bluetooth, 1000DPI, Blanco |
| CREALITY | 4459 | Creality Resina para Impresora 3D 3302020027, Rígida Estándar, 1Kg, Blanco |
| BEHRINGER | 4259 | Behringer Sistema de Grabación PODCASTUDIO 2 USB, incluye Micrófono, Audífonos y Mezclador Premium |
| TRUPER | 4149 | Truper Sopladora SOPLA-960, 960W, Naranja/Negro |
| FLUKE | 3789 | Fluke Termómetro IR 62 MAX, -30 - 500°C |
| PANDUIT | 3579 | Panduit Placa de Pared Ciega Universal, Blanco |
| INDIANA | 3539 | Indiana Cable de Cobre para Instalación de Pararrayos, 1/0 AWG, 19 Hilos, 15 Metros, Negro |
| POLY | 3519 | Poly Teléfono de Diadema CT14, Inalámbrico, DECT 6.0, Negro |
| MINELAB | 3299 | Minelab Detector de Metal Portátil Go Find 11, Sonido Ajustable |
| BELDEN | 3289 | Belden Panel de Parcheo Cat6 KeyConnect, 1U, 24 Puertos, Negro |
| INTEL | 3259 | Intel NUC Kit NUC7PJYHN, Intel Pentium Silver J5005 1.50GHz \(Barebone\) - Incluye Cable de Alimentación |
| ASTRON | 3219 | Astron Fuente de Poder Conmutada SS-12, Entrada 100 - 240V, Salida 13,8V, 12A |
| D-LINK | 3139 | D-Link Cámara PT para Bebé DCS-850L Lite, Inalámbrico |
| EPEVER | 3019 | EPEVER Controlador de Carga Solar XTRA 3415N, 12 - 48V, 30A |
| XZEAL | 3009 | XZEAL Webcam XZ200, 1920 x 1080 Pixeles, Negro |
| ALPHACOOL | 2989 | Alphacool Placa de Respaldo GPX Eisblock, LED, para NVIDIA RTX 2080/RTX 2080 Ti/RTX 2070 |
| MOXA | 2889 | Moxa Servidor Serial TCC-100, 1x RS-232/422/485 DB9, Negro |
| WESTERN DIGITAL | 2829 | SSD Western Digital WD Green, 1TB, SATA III, 2.5", 7mm |
| KOBLENZ | 2679 | Koblenz Supresor de Picos SS-550 USB, 5x NEMA 5–15R, 2x USB, 550 Joules, Gris |
| STEREN | 2490 | Steren Tubo de Soldadura  SOL60-020, 17g, Estaño/Plomo \(60/40\) |
| ASSA ABLOY | 2479 | Assa Abloy Smart Hub para Cerraduras, Inalámbrico, WiFi, Blanco |
| AUDIOLABS | 2439 | Audiolabs Amplificador para Auto ADL-C1100.1D, 1 Canal, 2000W RMS, Negro |
| ALTRONIX | 2439 | Altronix Tarjeta de Control de Alimentación ACM8, Entrada 12 - 24V, 8 salidas AC |
| MIDEA | 2409 | Midea Lavadora de Carga Vertical MLTS101M2SGDW, 10.1Kg, Negro/Blanco |
| AEROCOOL | 2399 | Ventilador Aerocool Air Frost Plus LED RGB, 124mm, 1500RPM, Negro |
| BALAMRUSH | 2369 | Tapete Gamer Balam Rush ULTIMATE, 12 x 12cm, Grosor 5mm, Negro/Rojo |
| BUFFALO | 2339 | Buffalo BRXL-PT6U2VB, Grabador de Blu-ray Portátil, BD-R 6x / DVD+R 8x / CD-RW 16x, Externo, Negro |
| NECNON | 2339 | Tablero Arcade Necnon NCA-6084 Fights, 6084 Juegos, Multicolor |
| STI | 2309 | STI Botón de Salida de Emergencia, Alámbrico, Amarillo, Texto en Inglés |
| ARUBA | 2309 | Aruba Cable R9D20A SFP+ Macho - SFP+ Macho, 3 Metro, Negro/Plata |
| ANCLO | 2219 | Anclo Tubo Flexible Galvanizado 1'', 30 Metros, Plata |
| TP-LINK | 2219 | TP-Link TG-3468 Tarjeta de Red PCI Express, Alámbrico, IEEE 802.3/3u/3ab, 802.3x, 802.1q/1p |
| BOSCH | 2209 | Bosch Tarjeta de Proximidad RFID, 8.5 x 5.4cm, Blanco, 25 Piezas |
| KAPTON | 2209 | Kapton Ecualizador Gráfico CR-231EQ, 31 Bandas, Púrpura/Negro |
| MIMOSA NETWORKS | 2209 | Mimosa Networks Radio de Backhaul Modular C5X, 8dBi, 4.9 - 6.4GHz - Requiere Adaptador PoE, se Vende por Separado |
| EC LINE | 2189 | EC Line EC-PM-58110, Kit Impresora de Tickets, Térmica Directa, USB, Negro - incluye Lector de Código de Barras |
| VICTORINOX | 2179 | Victorinox Navaja de Bolsillo Swiss Champ, 33 Usos, Rojo |
| BIXOLON | 2169 | Bixolon Pantalla POS Pole BCD-2000, USB 2.0, Negro |
| GRANDSTREAM | 2049 | Grandstream ATA HT814, 4 Puertos FXS, 2x RJ-45 |
| MIKROTIK | 2029 | MikroTik RouteBoard RB912UAG-5HPND, 300 Mbit/s, 1x RJ-45, 5GHz |
| YEASTAR | 2019 | Yeastar Tarjeta de Expansión YS-MDO2, 2 Canales FXO, para S412/S20/S50/S100/S300 |
| LUTRON | 1959 | Lutron Hub Repetidor de Señal Inalámbrico, Blanco |
| AMD | 1959 | Procesador AMD Ryzen 5 3600, S-AM4, 3.60GHz, 32MB L3 Cache, con Disipador Wraith Stealth |
| SANAIRE | 1939 | Sanaire Campana Phillax, 61cm, Gris |
| KÄRCHER | 1939 | Karcher Hidrolavadora a Presión K2 Classic, 1600psi, Amarillo |
| KINGSTON | 1929 | Memoria RAM Kingston DDR4, 2666MHz, 32GB, Non-ECC, CL19, SO-DIMM |
| CHEFMAN | 1899 | Chefman Freidora de Aire Turbo Fry, 7.5 Litros, Negro/Acero Inoxidable |
| SL PROLIGHT | 1829 | SL Prolight Reflector LED Flood Perfetti, 150W, Negro |
| RASPBERRY | 1799 | Raspberry Lente para Cámara Thelephoto, 16mm, 10MP, para Raspberry Pi HQ |
| POWER SONIC | 1759 | Power Sonic Batería de Respaldo UL PS-12260-F2, 12V, 26Ah, para Alarmas de Incendio |
| WINLAND | 1759 | Winland Sensor para Nivel de Agua WB-200, Alámbrico, Blanco |
| GAMA ITALY | 1729 | Gama Italy Depiladora Oasis Supreme, 8 Pasos, 2 Velocidades, Rosa/Blanco |
| BLACK & DECKER | 1699 | Black & Decker Sierra Caladora KS501, 420W, Naranja |
| SANDISK | 1659 | SSD Externo SanDisk Portable, 1TB, USB C, Negro |
| IMOU | 1649 | Imou Cámara IP Smart WiFi Domo IR para Interiores Ranger 2C, Inalámbrico, 1920 x 1080 Pixeles, Día/Noche - Incluye Cámara Imou Cue WiFi |
| ANTROLITE | 1639 | Antrolite Soporte para Tableta 6”-12”, Negro |
| ROYAL | 1619 | Royal Lampara Dectectora de Billetes Falsos ELEROYDETBUV1, Luz Ultravioleta, Detector magnético, Negro |
| ELECTRONIC ARTS | 1619 | FIFA 23, Xbox Series X |
| LEXMARK | 1609 | Lexmark Unidad de Imagen 50F0Z00, 60.000 Páginas |
| XP-PEN | 1609 | Tableta Gráfica XP-PEN Deco Fun L, 25.4 x 159.2cm, Alámbrico, USB-C, Rojo Carmín |
| WAVESHARE | 1609 | Waveshare Pantalla 5" para Placas de Desarrollo Raspberry Pi WS-18396, 800 x 480 Pixeles, Negro |
| VERBATIM | 1609 | Verbatim Torre de Discos Virgenes para DVD, DVD+R, 8x, 50 Discos \(97000\) |
| HYPERLUX | 1589 | Hiperlux Iluminador Infrarrojo 90°, hasta 45 Metros, Beige |
| KIWO | 1589 | KIWO Mini Home Theater AAHTD20, Bluetooth, Alámbrico, 2 Canales, 30W RMS, Negro, CD Player Incluido |
| WESTINGHOUSE | 1579 | Westinghouse Parrilla Grill Eléctrica Panini, Antiadherente, 1400W, Negro |
| RHINO | 1549 | Rhino Báscula Electrónica BAR-8RS, hasta 40Kg, Negro/Gris |
| YLI ELECTRONIC | 1539 | YLI Electronic Cerradura Electromagnética YM-500NW, 6 x 18.5cm, 500Kg |
| TRIPP LITE | 1539 | Tripp Lite Cable VGA Coaxial para Monitor, VGA \(D-Sub\) Macho - VGA \(D-Sub\) Macho, 7.62 Metros, Negro |
| HYPE | 1489 | Proyector Portátil Hype M24 3LCD, 800x480, máx. 1200 Lúmenes, con Bocinas, Amarillo |
| VSG | 1469 | Teclado Gamer VSG Mintaka RGB 60%, Teclado Mecánico, Switch Kailh Blue, Alámbrico, Blanco \(Español\) |
| PEAK TOUR | 1459 | Peak Tour Maletín de Poliéster Windsor para Laptop 15.6", Negro |
| TECNOLITE | 1419 | Tecnolite Lámpara LED para Techo Empotrable Regulus, Interiores, Luz de Día, 7W, 500 Lúmenes, Blanco, para Casa |
| REMINGTON | 1419 | Remington Secadora D24A Supercare Pro, 2 Velocidades, 1900W, Negro |
| COMMSCOPE | 1359 | CommScope Kit de Montaje Punta Torre, Plata |
| ACCO | 1359 | Acco Separador 442, 5 Divisiones, Blanco |
| AMAZON | 1359 | Amazon Kit de Echo Dot Asistentes de Voz 3ra Generación, Inalámbrico, WiFi, Bluetooth, 2 Piezas |
| TWELVE SOUTH | 1309 | Twelve South Funda SuitCase para MacBook Pro/Air 16", Gris |
| EPOS | 1289 | EPOS Dispositivo para Descolgar HSL 10 II, Negro |
| KENSINGTON | 1279 | Kensington Filtro de Privacidad MagPro Elite para MacBook Pro 16", Negro |
| ACTIVISION | 1269 | Call of Duty WWII Gold Edition, Xbox One ― Producto Digital Descargable |
| ALCTRON | 1259 | Alctron Interfaz de Audio USB XU-2 MKII, USB, XLR, Negro |
| DEEPCOOL | 1249 | Disipador CPU DeepCool AK620, 120mm, 500-1850RPM, Negro |
| OKY | 1249 | OKY Pinza Robótica OS-06016, 2° Libertad, Aluminio |
| GBC | 1219 | GBC Guillotina Classiccut Lite de 12'', hasta 10 Hojas |
| JBL | 1189 | JBL Subwoofer Stage3 8627, 50W RMS, 65 - 20.000Hz, 6 x 8”, Negro |
| STEEL PRO | 1189 | Steel Pro Autoestéreo XZR-070, FM/MP3, Bluetooth/USB, Negro |
| PCTEL | 1149 | PCTEL Antena para Radio BOA24006-NF, 2400 - 5MHz, 6dBi |
| CINSA | 1149 | Cinsa Batería de Cocina Yubicela, Acero Vitrificado, Antiadherente, 4 Piezas, Blanco |
| MANHATTAN | 1139 | Manhattan Video Splitter HDMI, 2 Puertos HDMI |
| BESTEK | 1129 | Bestek Inversor de Corriente MRZ3011HU, 300W, Entrada 15V, Salida 120V,  2 Contactos |
| AJAX | 1129 | AJAX Detector de Ruptura de Vidrio GlassProtect, Inalámbrico, hasta 9 Metros, Blanco |
| SYSCOM | 1119 | Syscom Brazo para Torre Arriostrada Tipo Bastón, para STZ30G/STZ35G/STZ45G |
| RCI | 1089 | RCI Estación Manual de Emergencia 904PB, Alámbrico, Azul |
| ZAGG | 1009 | Zagg Protector de Pantalla para iPad Pro 11 11" Glass+ Visionguard, Transparente |
| CABLEMOD | 999 | Cablemod Kit de Cables de Poder PCI Express, Blanco, incluye 1x Cable ATX 24-pin/1x EPS 8-pin/1x EPS 4+4-pin/1xPCI-E 16-pin a 3x8-pin |
| NATIVE UNION | 969 | Native Union Funda para AirPods 3ra Gen., Negro |
| EVGA | 969 | EVGA PRO SLI Bridge HB de 4 Slots, 120mm |
| TRAMONTINA | 959 | Tramontina Juego de Cuchillos Cronos, 3 Piezas, Acero Inoxidable |
| MODAMOB | 939 | Modamob Silla Canis, Respaldo de Rejilla, Negro |
| HAMILTON BEACH | 929 | Hamilton Beach Chocomilera DrinkMaster, 0.8 Litros, 2 Velocidades, Negro |
| MERIVA TECHNOLOGY | 919 | Meriva Technology Cable BNC Macho - BNC Macho, 18 Metros, Negro |
| TARGUS | 889 | Targus Funda Universal SafeFit para Tablet 8.5", Giro 360°, Negro |
| PRECISION | 839 | Precision Kit de Herramientas para Reparaciones en General |
| FOSET | 835 | Foset Filtro de Agua PURA-P3, Blanco - Elimina 99.99% de Bacterias |
| GEAR4 | 799 | Gear4 Funda Crystal Palace Clear para iPhone 7/8/SE, Transparente |
| MOLOTOW | 799 | Molotow Válvula 900077, 1.5cm, Azul |
| CONAIR | 709 | Conair Tina masajeador para Pies FB5XBCRES, Rosa/Blanco |
| PRETUL | 699 | Pretul Rotomartillo ROTO-1/2P6, 1/2", Alámbrico, 550W, Amarillo |
| SECO-LARM | 689 | Seco-Larm Módulo Relevador SR-2112-C7AQ/10, 7A, 12-24V |
| UGREEN | 659 | Ugreen Hub USB C 3.2 - 4x USB A 3.0, 1x HDMI, Gris |
| NEXTEP | 639 | Nextep Revistero de Metal NE-163A, 6 Ranuras, 2 Bandejas, Negro |
| FOY | 599 | Foy Disco para Sierra 143565, 14", 60 Dientes, para Madera/Madera Laminada/PVC |
| GOOGLE | 599 | Google Chromecast Gen 3, Full HD, WiFi, HDMI, Negro \(Inglés\) |
| BOWER | 599 | Bower Kit Filtro para Cámara Ultravioleta Polarizado, 3 Filtros, Negro - incluye Estuche |
| RESIDEO | 579 | Resideo Control Remoto de 4 Botones, Inalámbrico, Negro, Compatible con Panel ProSeries |
| TXPRO | 579 | TXPRO Funda de Plástico TXCDEP450, Negro, para Motorola DEP450 |
| OVALTECH | 579 | Ovaltech Brazo de Pared para Monitor 17" - 27", máx. 7kg, Negro |
| COOLER MASTER | 569 | Cooler Master Disipador para VGA Hydra 8800, para NVIDIA GeForce 8800GTX/Ultra, 1800RPM |
| XIAOMI | 559 | Xiaomi Selfie Stick, Bluetooth, Gris |
| CORSAIR | 559 | Memoria RAM Corsair DDR3, 1066MHz, 4GB, CL7, SO-DIMM, para Mac |
| HYPERX | 549 | HyperX Set de 19 Piezas Rubber, Rosa |
| Norton LifeLock | 529 | Norton Utilities Ultimate, 1 Usuario, 10 Dispositivos, 1 Año, Windows ― Producto Digital Descargable |
| CENTURY | 509 | Century Tag para Ropa T005, Blanco, 100 Piezas |
| MAE | 509 | Mae Tachuela PVC, Paquete de 100 Piezas, Blanco |
| KLEIN TOOLS | 469 | Klein Tools Grapas con Aislamiento 450-003, 9 x 15mm, para Cables NM \(Romex\) 14/3/14/3G/12/3/Cables de 11/32''/19/32'' |
| JENDRIX | 467 | Jendrix Pinza de Compresión PY-107, F/BNC/RG-58/RG-59, Rojo/Negro |
| EZVIZ | 459 | Ezviz Contacto Magnético WiFi T2C para Puerta/Ventana, Interiores, Inalámbrico, Blanco |
| YAELTEX | 455 | Yaeltex Módulo Kilomux tipo Fader F41, para Placas de Desarrollo, 1 Pieza |
| DERWENT | 454 | Derwent Lápiz de Grafito, Caja Metálica con 12 Piezas |
| PERFECT CHOICE | 448 | Perfect Choice Mochila Essentials para Laptop 15''-17'', Negro |
| TIMCO | 446 | Timco Hervidor de Agua Eléctrica JEV02, 1.7 Litros, 1200W, Negro |
| VICA | 444 | Vica Multicontacto SUPVIC050, 3 Salidas, 4x USB, Blanco |
| BROBOTIX | 439 | Brobotix Tarjeta PCI Express Serial DB9, 2 Puertos x RS-232 |
| IFROGZ | 432 | iFrogz Protector de Pantalla Glassguard para iPhone X, Transparente |
| ESSELTE | 429 | Esselte Sobre Coin 75007, Paquete de 500 Piezas, 8.9 x 16.5cm, Color Manila |
| BEEPER | 425 | Beeper Desarmador de Bola y Puntas, 6 Piezas, Negro |
| TAURUS | 424 | Taurus Ventilador Bolt, 2 Velocidades, 16", Blanco |
| MASTERCHEF | 412 | MasterChef Molino de Granos de Café y Especias MKCG1SP, 150W, Acero Inoxidable |
| CHOETECH | 388 | Choetech Cargador Inalámbrico de Carga Rápida T559-F, 15W, Negro |
| IML | 381 | IML Antena para Televisión Yagui ABC40R, Exterior, UHF/VHF/HDTV, Aluminio |
| INTELLINET | 374 | Intellinet Probador de Cables de Red, RJ-11/RJ-45, 4 LEDs |
| FRAGA | 373 | Fraga Parrilla de Gas P502, 2 Quemadores, Negro |
| CELICA | 366 | Celica Calculadora Científica FX-82MS, 10+2 Dígitos, Batería/Energía Solar, Negro |
| LITE-ON | 361 | Lite-On iHAS124 Quemador de DVD, DVD-R 24x / DVD+RW 8x, Interno, SATA, Negro \(Bulk\) |
| RAIDMAX | 359 | Raidmax Kit de Disipador RGB para RAM MX-902F, 5V, Negro |
| RADOX | 359 | Radox Trompeta para Perifoneo, 12", Exterior, Gris - no incluye Unidad/Driver |
| KRO | 341 | KronalinE Rollo de Papel para Impresora de Inyección de Tinta, N2", 75g/m², 35.8" x 164' |
| XSS | 336 | XSS Micrófono CM-158B, Alámbrico, XLR, Negro |
| KASPERSKY | 327 | Kaspersky Anti-Virus 2017, 1 Usuario, 1 Año, Windows |
| MISIK | 318 | Misik Radio Despertador MR420, AM/FM, Negro |
| AZOR | 316 | Azor Sacapuntas Manual 305-A, Azul/Amarillo |
| YEALINK | 314 | Yealink Adaptador de Corriente PS 12V1A, para Teléfonos IP T18P/T2/T41P/T42G |
| ACTECK | 311 | Acteck Smartwatch Motion Sport SW250, Touch, Bluetooth 5.0, Android/iOS, Negro - Resistente a Salpicaduras y Polvo |
| ENERGIZER | 308 | Energizer Pilas No-Recargables AA, 1.5V, 8 Piezas |
| TECHZONE | 306 | TechZone Maletín de Nílon TZ16BCP33 para Video Proyectores, Negro |
| STYLOS | 305 | Stylos Tripié para Bocina STASOX1B, hasta 102cm, Negro |
| ADATA | 296 | Memoria USB Adata UR340, 128GB, USB 3.2, Lectura 100 MB/s, Negro |
| RF INDUSTRIES | 292 | RF Industries Conector TNC Macho de Anillo Plegable para Cable RG-11/U |
| MIRATI | 283 | Mirati Smart Plug MCI2, WiFi, 1 Conector, 1100W, 10A, Blanco |
| CHAROFIL | 282 | Charofil Ménsula Omega Tipo L Inteligente, 31cm, Metal |
| ENSON | 273 | Enson Gabinete Metálico LINCE10 para Proteger Sirena de 15W |
| X-MEDIA | 271 | X-Media Adaptador USB 3.0 Macho - IDE, Negro |
| HAHNEMUHLE | 266 | Hahnemühle Cuaderno Sketch Diary Black, A5, 14.8 x 21cm, 60 Hojas, Negro, para Escribir |
| ATL | 263 | ATL Set de Pastillas Acuarelas para Arte con Pincel G101, 12 Colores |
| ROYAL TALENS | 248 | Royal Talens Tinta Acuarela con Gotero Ecoline, 30ml, Sepia Oscuro No. 440 |
| SAXXON | 244 | Saxxon Adaptador de Corriente PSU1205D, Entrada 100 - 240V, Salida 12V |
| PROLICOM | 236 | Prolicom Paños Humedos TOWEL-70, para Pantallas LCD/TFT/Plasma, 2 Piezas |
| FUSSION ACUSTIC | 235 | Fussion Acustic Transmisor FM para Auto RF-1511WH, USB-A, Negro/Blanco |
| EKCO | 233 | Ekco Cacerola, 16cm, Esmalte Vitrificado, Azul |
| GAME FACTOR | 220 | Game Factor Pasta Térmica TP300, -250 - 350 °C, 2 Gramos |
| AMERICAN | 219 | American Batidora de Mano 9975, 120W, 7 Velocidades, Blanco/Gris |
| MAKITA | 216 | Makita Brocasierra Bimetálica D-21783, 3-5/8” |
| POLITEC | 214 | Politec Pintura Acrílica Metálica para Arte Línea 700, 250ml, Bronce, No. 702 |
| DATAPAC | 186 | Cinta Datapac DP-031 Negro |
| MAXELL | 156 | Maxell Cartucho de Limpieza HS-4 DDS, 4mm |
| PELIKAN | 136 | Pelikan Goma de Migajón Tipo Bloque, Blanco, 20 piezas |
| EUROCOLORS | 132 | Eurocolors Fólder PU0003, Paquete de 25 Piezas, Tamaño Carta, Surtido Neón |
| ROMMS | 102 | Romms Pila Telefónica Recargable, 3.6V, 600mAh |
| SAKURA | 100 | Sakura Marcador Pen Touch 42100, Punto Extra Fino, Blanco |
| CASE LOGIC | 98 | Case Logic Estuche para Cámara Digital, Negro |
| BLECK | 98 | Bleck Banda Extensible para Smartband, Azul |
| SFIRE | 81 | SFire Cople Recto para Tubería de Aspiración, Rojo |
| SPARKFUN | 55 | Sparkfun Kit de Jumpers Hembra - Hembra, 20 Piezas, Multicolor |
| PILOT | 41 | Pilot Desengrapador de Acero No.6, Negro |





Excersice 2
------------

### Show the average prices

    SELECT m.title as Manufacturer, avg(a.price) as AVGPrice
    FROM articles AS a
    JOIN manufacturers AS m ON a.manufacturer_id = m.id
    GROUP BY m.title
    ORDER BY max(a.price) DESC;

First, two columns are selected to be displayed in the results. The first column shows the title of the manufacturer (renamed as "Manufacturer"), and the second column shows the average price of the articles (renamed as "AVGPrice"). The avg(a.price) function calculates the average price of all articles associated with each manufacturer.

Articles (aliased as a) and manufacturers (aliased as m) are joined. The join is made on the condition that the manufacturer_id field in the articles table matches the id field in the manufacturers table. This means it combines rows from these two tables where the specified condition is true.

The grouping (groups the results by the manufacturer's title) is necessary because the query calculates an aggregate function (average) on the articles' prices, requiring the data to be partitioned by manufacturer.  Finally, the results are ordered by the maximum price of articles for each manufacturer. 

**Results:**

| Manufacturer        | AVGPrice           |
|:--------------------|:-------------------|
| HP ENTERPRISE       | 52964.555555555555 |
| DELL                | 21516.282608695652 |
| HP                  | 21216.674496644297 |
| MSI                 | 32759.54054054054  |
| APPLE               | 34546.83720930233  |
| TOUGHBOOK PANASONIC | 83302.33333333333  |
| ASUS                | 18834.289256198346 |
| LENOVO              | 21878.706270627063 |
| VSSL                | 60989              |
| ALIENWARE           | 46249              |
| DKS DOORKING        | 51689              |
| GIGABYTE            | 20954.166666666668 |
| ELO TOUCHSYSTEMS    | 43659              |
| SAMSUNG             | 15734              |
| ACER                | 15936.727272727272 |
| PNY                 | 36849              |
| EVOLIS              | 35539              |
| ONKYO               | 35009              |
| AORUS               | 30269              |
| XPG                 | 16398              |
| BROTHER             | 7924.4             |
| HUAWEI              | 19546.272727272728 |
| EPSON               | 6744.555555555556  |
| CISCO               | 25039              |
| StarTech.com        | 5292.571428571428  |
| UBIQUITI NETWORKS   | 7880               |
| CYBERPOWER          | 21709              |
| DYNABOOK            | 15324              |
| BENQ                | 20679              |
| HONOR               | 19369              |
| GRIZZLY             | 18629              |
| WEBOOST             | 9719               |
| LANIX               | 9403.285714285714  |
| URREA               | 5181.083333333333  |
| PROVISION ISR       | 7985               |
| XEROX               | 5659               |
| ACCESSPRO           | 5109               |
| DATAPRODUCTS        | 14969              |
| HIKMICRO            | 14509              |
| MICROSOFT           | 3659.5             |
| SONY                | 6305               |
| ZEBRA               | 3820.7             |
| WHIRLPOOL           | 11659              |
| HONEYWELL           | 4924               |
| LG                  | 6669               |
| CANON               | 6504               |
| MEGALUZ             | 5175.666666666667  |
| DAHUA               | 2476.7272727272725 |
| EPCOM               | 1723.2             |
| VORAGO              | 4820.666666666667  |
| LINKSYS             | 7899               |
| GATEWAY             | 5920.428571428572  |
| JABRA               | 5009               |
| SOLAX               | 9329               |
| GHIA                | 4700.6             |
| HIKVISION           | 2436               |
| TOTAL GROUND        | 8369               |
| HYUNDAI             | 5114.263157894737  |
| TACX                | 8299               |
| BEA                 | 8159               |
| SHURE               | 7889               |
| BIRD TECHNOLOGIES   | 5449               |
| RHEEM               | 7399               |
| NINTENDO            | 7309               |
| ALLIED TELESIS      | 4749               |
| GARMIN              | 6999               |
| ALIEN               | 3690.5             |
| ELGATO              | 3814               |
| ZKTECO              | 3621.5             |
| SURTEK              | 2118               |
| QIAN                | 3706               |
| FELLOWES            | 3792.3333333333335 |
| BINDEN              | 1499.8             |
| POSLINE             | 3149               |
| HISENSE             | 5449               |
| PANASONIC           | 3671.6666666666665 |
| LINKEDPRO           | 2174.8333333333335 |
| SEAGATE             | 3084               |
| THOMSON             | 3536.5             |
| ABB                 | 3234               |
| LOGITECH            | 1556.2             |
| CREALITY            | 1555.75            |
| BEHRINGER           | 2909               |
| TRUPER              | 1514.6             |
| FLUKE               | 3789               |
| PANDUIT             | 1158.6666666666667 |
| INDIANA             | 3539               |
| POLY                | 2204.25            |
| MINELAB             | 3299               |
| BELDEN              | 3289               |
| INTEL               | 3259               |
| ASTRON              | 3219               |
| D-LINK              | 1680.5             |
| EPEVER              | 3019               |
| XZEAL               | 1661               |
| ALPHACOOL           | 2989               |
| MOXA                | 1533               |
| WESTERN DIGITAL     | 1705.6666666666667 |
| KOBLENZ             | 1569.6666666666667 |
| STEREN              | 695.0714285714286  |
| ASSA ABLOY          | 2059               |
| ALTRONIX            | 2439               |
| AUDIOLABS           | 2439               |
| MIDEA               | 1949               |
| AEROCOOL            | 1299.5             |
| BALAMRUSH           | 1489               |
| NECNON              | 1400.5             |
| BUFFALO             | 2339               |
| STI                 | 2309               |
| ARUBA               | 2309               |
| TP-LINK             | 862.8571428571429  |
| ANCLO               | 2219               |
| MIMOSA NETWORKS     | 2209               |
| BOSCH               | 2209               |
| KAPTON              | 1236.5             |
| EC LINE             | 1429               |
| VICTORINOX          | 2179               |
| BIXOLON             | 2169               |
| GRANDSTREAM         | 2049               |
| MIKROTIK            | 2029               |
| YEASTAR             | 2019               |
| AMD                 | 1959               |
| LUTRON              | 1959               |
| KÄRCHER             | 1939               |
| SANAIRE             | 1939               |
| KINGSTON            | 726.3333333333334  |
| CHEFMAN             | 1899               |
| SL PROLIGHT         | 1829               |
| RASPBERRY           | 779                |
| POWER SONIC         | 1759               |
| WINLAND             | 1684               |
| GAMA ITALY          | 1729               |
| BLACK & DECKER      | 818                |
| SANDISK             | 1659               |
| IMOU                | 1649               |
| ANTROLITE           | 718.75             |
| ELECTRONIC ARTS     | 1619               |
| ROYAL               | 1058.5             |
| LEXMARK             | 1299               |
| VERBATIM            | 708                |
| XP-PEN              | 1609               |
| WAVESHARE           | 1609               |
| KIWO                | 1589               |
| HYPERLUX            | 1589               |
| WESTINGHOUSE        | 1021               |
| RHINO               | 1549               |
| YLI ELECTRONIC      | 1539               |
| TRIPP LITE          | 561.25             |
| HYPE                | 1489               |
| VSG                 | 1469               |
| PEAK TOUR           | 1004               |
| TECNOLITE           | 762.6666666666666  |
| REMINGTON           | 1234               |
| COMMSCOPE           | 778.5              |
| AMAZON              | 1359               |
| ACCO                | 944                |
| TWELVE SOUTH        | 1309               |
| EPOS                | 834                |
| KENSINGTON          | 1279               |
| ACTIVISION          | 1269               |
| ALCTRON             | 1259               |
| DEEPCOOL            | 1249               |
| OKY                 | 1249               |
| GBC                 | 728                |
| JBL                 | 1189               |
| STEEL PRO           | 1189               |
| CINSA               | 1149               |
| PCTEL               | 1149               |
| MANHATTAN           | 415.1111111111111  |
| BESTEK              | 1129               |
| AJAX                | 1129               |
| SYSCOM              | 1119               |
| RCI                 | 1089               |
| ZAGG                | 1009               |
| CABLEMOD            | 999                |
| EVGA                | 969                |
| NATIVE UNION        | 839                |
| TRAMONTINA          | 600                |
| MODAMOB             | 939                |
| HAMILTON BEACH      | 929                |
| MERIVA TECHNOLOGY   | 541                |
| TARGUS              | 613                |
| PRECISION           | 500.5              |
| FOSET               | 835                |
| GEAR4               | 794                |
| MOLOTOW             | 355.5              |
| CONAIR              | 709                |
| PRETUL              | 699                |
| SECO-LARM           | 407.5              |
| UGREEN              | 380.5              |
| NEXTEP              | 307                |
| GOOGLE              | 599                |
| BOWER               | 549                |
| FOY                 | 599                |
| RESIDEO             | 579                |
| OVALTECH            | 579                |
| TXPRO               | 455.5              |
| COOLER MASTER       | 569                |
| XIAOMI              | 482                |
| CORSAIR             | 416.6666666666667  |
| HYPERX              | 549                |
| Norton LifeLock     | 529                |
| CENTURY             | 509                |
| MAE                 | 315.6666666666667  |
| KLEIN TOOLS         | 469                |
| JENDRIX             | 282                |
| EZVIZ               | 459                |
| YAELTEX             | 455                |
| DERWENT             | 378                |
| PERFECT CHOICE      | 429                |
| TIMCO               | 446                |
| VICA                | 444                |
| BROBOTIX            | 218                |
| IFROGZ              | 409.5              |
| ESSELTE             | 317.6666666666667  |
| BEEPER              | 362.5              |
| TAURUS              | 349                |
| MASTERCHEF          | 412                |
| CHOETECH            | 388                |
| IML                 | 381                |
| INTELLINET          | 312.5              |
| FRAGA               | 373                |
| CELICA              | 366                |
| LITE-ON             | 361                |
| RAIDMAX             | 359                |
| RADOX               | 260.75             |
| KRO                 | 341                |
| XSS                 | 336                |
| KASPERSKY           | 327                |
| MISIK               | 318                |
| AZOR                | 194.33333333333334 |
| YEALINK             | 314                |
| ACTECK              | 226                |
| ENERGIZER           | 245.33333333333334 |
| TECHZONE            | 306                |
| STYLOS              | 305                |
| ADATA               | 245.66666666666666 |
| RF INDUSTRIES       | 292                |
| MIRATI              | 283                |
| CHAROFIL            | 282                |
| ENSON               | 273                |
| X-MEDIA             | 271                |
| HAHNEMUHLE          | 266                |
| ATL                 | 184.5              |
| ROYAL TALENS        | 248                |
| SAXXON              | 244                |
| PROLICOM            | 236                |
| FUSSION ACUSTIC     | 188.8              |
| EKCO                | 233                |
| GAME FACTOR         | 201                |
| AMERICAN            | 219                |
| MAKITA              | 216                |
| POLITEC             | 160.5              |
| DATAPAC             | 186                |
| MAXELL              | 156                |
| PELIKAN             | 136                |
| EUROCOLORS          | 132                |
| ROMMS               | 102                |
| SAKURA              | 88                 |
| BLECK               | 98                 |
| CASE LOGIC          | 98                 |
| SFIRE               | 81                 |
| SPARKFUN            | 55                 |
| PILOT               | 41                 |




Excercise 3
------------

### Show how many products there are in each category

    SELECT c.title as Categories, count(a.title) as NumberOfPrducts
    FROM articles AS a
    JOIN articles_categories as ac on a.id= ac.article_id
    JOIN categories AS c ON ac.category_id = c.id
    GROUP BY c.title;

A selection is done with the title from the categories table (aliased as c) and renames it as "Categories". It also counts the number of titles in the articles table (aliased as a) and labels this count as "NumberOfProducts". Essentially,  the data will be fetched from the articles table, which is given the alias a for use in this query.

Then articles_categories table (aliased as ac) and the articles table are joined. The join is made where the article ID in the articles table matches the article ID in the articles_categories table. 

Another join is made, this time connecting the categories table (aliased as c) with the articles_categories table. The connection is based on matching the category IDs.  Because of the grouping, the count of article titles will be organized by each unique category, essentially giving the number of articles per category.

**Results:**

| Categories                                    | NumberOfPrducts |
|:----------------------------------------------|:----------------|
| Accesorios Apple Music                        | 1               |
| Accesorios para Apple Watch                   | 1               |
| Accesorios para Barreras Vehiculares          | 1               |
| Accesorios para Cautines                      | 1               |
| Accesorios para Enfriamiento Líquido          | 1               |
| Accesorios para Estaciones de Trabajo         | 1               |
| Accesorios para Gabinetes                     | 1               |
| Accesorios para Impresión 3D                  | 1               |
| Accesorios para Instalación                   | 1               |
| Accesorios para Interruptores                 | 1               |
| Accesorios para Micrófonos                    | 1               |
| Accesorios para Nintendo Switch               | 1               |
| Accesorios para Puertas de Emergencia         | 1               |
| Accesorios para Smartwatch                    | 1               |
| Accesorios para Torres Autosoportadas         | 1               |
| Accesorios para Videoporteros                 | 1               |
| Accesorios para Xbox Series X/S               | 1               |
| Accesorios Playstation 4                      | 1               |
| Accesorios PlayStation 5                      | 1               |
| Accesorios Xbox One                           | 1               |
| Access Points                                 | 1               |
| Acopladores                                   | 1               |
| Acuarelas en Pastilla                         | 1               |
| Adaptadores / Cables para Apple               | 1               |
| Adaptadores Audio AUX                         | 1               |
| Adaptadores Audio USB                         | 1               |
| Adaptadores de Audio                          | 1               |
| Adaptadores de Discos Duros                   | 2               |
| Adaptadores de Energía Universal              | 1               |
| Adaptadores de Red para Impresoras            | 1               |
| Adaptadores de Red para Proyectores           | 1               |
| Adaptadores de Red USB                        | 1               |
| Adaptadores PC IDE                            | 1               |
| Adaptadores PC SATA                           | 1               |
| Adaptadores PC Teclado                        | 1               |
| Adaptadores PC USB                            | 1               |
| Adaptadores PoE                               | 1               |
| Adaptadores Video DisplayPort                 | 1               |
| Adaptadores Video DVI                         | 1               |
| Adaptadores Video HDMI                        | 1               |
| Adaptadores Video VGA / HD15                  | 1               |
| Adaptadores XLR                               | 1               |
| Aires Acondicionados                          | 1               |
| AirPods                                       | 1               |
| Alisadores y Rizadores                        | 1               |
| All in One                                    | 1               |
| Almacenamiento MSA                            | 2               |
| Almacenamiento NAS                            | 2               |
| Almacenamiento SAS                            | 2               |
| Altavoces                                     | 1               |
| Amplificadores                                | 1               |
| Amplificadores de Celular                     | 1               |
| Amplificadores y Receptores AV                | 1               |
| Antenas                                       | 1               |
| Antenas Móviles                               | 1               |
| Antenas para Amplificadores                   | 1               |
| Antenas para Televisión                       | 1               |
| Antivirus                                     | 1               |
| Apple Pencil                                  | 1               |
| Apple TV                                      | 1               |
| Apple Watch                                   | 1               |
| Archivos Expandibles                          | 1               |
| Asistentes de Voz                             | 2               |
| Aspersores y Pistolas de Riego                | 1               |
| Aspiradoras                                   | 1               |
| Atenuadores                                   | 1               |
| Audífonos Intrauriculares                     | 1               |
| Autoestéreos                                  | 1               |
| Backhauls                                     | 1               |
| Bafles y Subwoofers Profesionales             | 1               |
| Bandejas y Alimentadores                      | 1               |
| Barebones                                     | 1               |
| Barreras Vehiculares                          | 1               |
| Báscula Corporal                              | 1               |
| Básculas Comerciales                          | 1               |
| Bases de Carga                                | 2               |
| Bases para Audífonos                          | 1               |
| Bases para PC's                               | 1               |
| Bases para Portátiles                         | 1               |
| Bases y Montajes                              | 1               |
| Bastidores y Marcos                           | 1               |
| Baterías de Cocina                            | 1               |
| Baterías para Teléfonos Convencionales        | 1               |
| Baterías Selladas                             | 1               |
| Batidoras                                     | 1               |
| Blocks, Cuadernos y Libros Artísticos         | 1               |
| Bluetooth                                     | 1               |
| Bobinas                                       | 1               |
| Bobinas de Filamento                          | 1               |
| Bocinas                                       | 2               |
| Bocinas para Sistemas de Audio                | 1               |
| Bolsas de Tinta                               | 1               |
| Bombas de Agua                                | 1               |
| Borradores                                    | 1               |
| Botones de Pánico                             | 1               |
| Botones de Salida                             | 1               |
| Brazos y Soportes                             | 1               |
| Brocas                                        | 1               |
| Burbujas Humeadas                             | 1               |
| Cabezales                                     | 1               |
| Cableado Estructurado                         | 1               |
| Cableado Estructurado para Servidores         | 2               |
| Cables                                        | 1               |
| Cables Coaxiales                              | 1               |
| Cables de Audio / Video AUX                   | 1               |
| Cables de Audio / Video BNC                   | 1               |
| Cables de Audio / Video DisplayPort           | 1               |
| Cables de Audio / Video DVI                   | 1               |
| Cables de Audio / Video HDMI                  | 1               |
| Cables de Audio / Video RCA                   | 1               |
| Cables de Audio / Video Toslink               | 1               |
| Cables de Audio / Video VGA                   | 1               |
| Cables de Poder \(Externo\)                   | 1               |
| Cables de Poder \(Interno\)                   | 1               |
| Cables Fibra Óptica                           | 1               |
| Cables KVM                                    | 2               |
| Cables para Auriculares                       | 1               |
| Cables para Radio                             | 1               |
| Cables Patch                                  | 1               |
| Cables PC FireWire                            | 1               |
| Cables PC KVM                                 | 1               |
| Cables PC Serial                              | 1               |
| Cables PC USB                                 | 1               |
| Cables PC VGA / HD15                          | 1               |
| Cables por Metro                              | 1               |
| Cables SFP+                                   | 1               |
| Cables XLR                                    | 1               |
| Cables y Adaptadores                          | 1               |
| Cables y Jumpers                              | 1               |
| Cafeteras                                     | 1               |
| Caja fuerte                                   | 1               |
| Cajas de Conexiones                           | 1               |
| Cajas de Herramientas                         | 1               |
| Cajas para Archivo                            | 1               |
| Cajones de dinero                             | 1               |
| Calculadoras                                  | 1               |
| Calentadores de Agua                          | 1               |
| Cámaras  digitales                            | 1               |
| Cámaras de Seguridad CCTV                     | 1               |
| Cámaras de Seguridad IP                       | 1               |
| Cámaras de video                              | 1               |
| Cámaras Ocultas                               | 1               |
| Cámaras Reflex                                | 1               |
| Cámaras Termicas                              | 1               |
| Candados                                      | 1               |
| Candados para Laptops                         | 1               |
| Cargadores de Dispositivos Móviles            | 1               |
| Cargadores de Pilas                           | 1               |
| Cargadores para Apple                         | 1               |
| Cargadores para Laptop                        | 1               |
| Cargadores para Teléfonos VoIP                | 1               |
| Cargadores Portátiles                         | 1               |
| Carpetas                                      | 1               |
| Cautines                                      | 1               |
| Celulares                                     | 1               |
| Cerraduras                                    | 1               |
| Cerraduras y Cerrojos para Control de Acceso  | 1               |
| Cestos y Basureros                            | 1               |
| Charolas para Racks y Gabinetes               | 2               |
| Chocomileras                                  | 1               |
| Cintas                                        | 1               |
| Cintas Adhesivas                              | 1               |
| Clips                                         | 1               |
| Clips para Radio                              | 1               |
| Colores                                       | 1               |
| Complementos para Videojuegos                 | 1               |
| Compresores                                   | 1               |
| Conectores                                    | 1               |
| Conectores Coaxiales                          | 1               |
| Conexiones en T                               | 1               |
| Congeladores                                  | 1               |
| Consolas Arcade                               | 1               |
| Consolas Nintendo Switch                      | 1               |
| Consolas Playstation 4                        | 1               |
| Consolas PlayStation 5                        | 1               |
| Consolas Xbox Series X/S                      | 1               |
| Contenedores de Desperdicio                   | 1               |
| Control de Acceso con Tarjeta                 | 1               |
| Control de Acceso Vehicular                   | 1               |
| Control de Acceso y Asistencia Biométrico     | 1               |
| Controladores de Carga Solar                  | 1               |
| Controladores Inalámbricos                    | 1               |
| Controles de Juego para PC                    | 1               |
| Controles para Videovigilancia                | 1               |
| Convertidores                                 | 1               |
| Convertidores de Medios                       | 1               |
| Cortadores                                    | 1               |
| CPE PtMP y PtP                                | 1               |
| Cubiertos                                     | 1               |
| Cuchillos                                     | 1               |
| Cutters                                       | 1               |
| Dados                                         | 1               |
| DDS                                           | 2               |
| Depiladoras                                   | 1               |
| Desarmadores y Puntas                         | 1               |
| Desengrapadoras                               | 1               |
| Destornilladores                              | 1               |
| Destructora de Papel                          | 1               |
| Detectora de Billetes Falsos                  | 1               |
| Detectores de Gas y Humo                      | 1               |
| Detectores de Metal                           | 1               |
| Detectores de Rotura de Vidrios               | 1               |
| Detectores de Temperatura                     | 1               |
| Detectores Fotoeléctricos                     | 1               |
| Detectores por Aspiración                     | 1               |
| Difusor de Aromas                             | 1               |
| Discos                                        | 1               |
| Discos CD                                     | 2               |
| Discos Duros Externos                         | 2               |
| Discos Duros Internos para Laptop             | 2               |
| Discos Duros Internos para PC                 | 2               |
| Discos Duros para NAS                         | 1               |
| Discos Duros para Servidores                  | 1               |
| Discos Duros para Videovigilancia             | 2               |
| Discos DVD                                    | 2               |
| Disipadores para CPU                          | 1               |
| Disipadores para VGA                          | 1               |
| Dispensadores de Agua                         | 1               |
| Dispositivos para Descolgar                   | 1               |
| Divisores de Video                            | 1               |
| Docking Stations                              | 1               |
| Drones                                        | 1               |
| Duplicadores de Datos y Soportes              | 1               |
| Ecualizadores / Crossover / Amplificadores    | 1               |
| Elementos para Wattmetros                     | 1               |
| Encuadernadoras                               | 1               |
| Energía Control de Acceso                     | 1               |
| Energía Foto y Video                          | 1               |
| Energía Impresión y Copiado                   | 1               |
| Energía para Cámaras y Grabadoras             | 1               |
| Energía para Radios                           | 1               |
| Energía para Sistemas de Alarmas              | 1               |
| Energia Punto de Venta \(POS\)                | 1               |
| Enfriadoras de Vinos                          | 1               |
| Enfriamiento Líquido                          | 1               |
| Enfriamiento para Servidores                  | 1               |
| Engargoladoras                                | 1               |
| Engrapadoras Industriales                     | 1               |
| Entrenadores para Ciclismo                    | 1               |
| Equipo para DJ                                | 1               |
| Escaleras                                     | 1               |
| Escáners                                      | 1               |
| Estaciones de Trabajo                         | 1               |
| Estaciones Manuales de Emergencia             | 1               |
| Estéreos                                      | 1               |
| Estilógrafos                                  | 1               |
| Estrobos y Luces Giratorias                   | 1               |
| Estufas y Campanas                            | 1               |
| Etiquetas POS                                 | 1               |
| Extensiones                                   | 1               |
| Extensores de Audio WiFi                      | 1               |
| Extensores de Rango                           | 1               |
| Extensores y Receptores de Vídeo              | 1               |
| Extractores y Exprimidores                    | 1               |
| Filtros de Agua                               | 1               |
| Filtros de privacidad                         | 1               |
| Filtros de Privacidad para Monitores          | 1               |
| Filtros para Cámara                           | 1               |
| Filtros para Purificadores de Aire            | 1               |
| Firewall                                      | 1               |
| Flash Fotográfico                             | 1               |
| Flexómetro                                    | 1               |
| Focos                                         | 2               |
| Focos Inteligentes                            | 1               |
| Fólder                                        | 1               |
| Foliadores                                    | 1               |
| Fotoconductores                               | 1               |
| Freidoras de Aire                             | 1               |
| Fuentes de Poder                              | 2               |
| Fuentes de Poder para Amplificadores          | 1               |
| Fuentes de Poder para Switches                | 1               |
| Fuentes Industriales CD                       | 1               |
| Fundas para AirTag                            | 1               |
| Fundas para Celulares                         | 1               |
| Fundas para iPad                              | 1               |
| Fundas para iPhone                            | 1               |
| Fundas para MacBook                           | 1               |
| Fundas para Radio                             | 1               |
| Fundas y Estuches                             | 1               |
| Fundas y Protectores POS                      | 1               |
| Fundas y Skins                                | 2               |
| Fusores                                       | 1               |
| Gabinetes                                     | 1               |
| Gabinetes de Discos Duros                     | 2               |
| Gateways y ATAs                               | 1               |
| Gatos Hidráulicos y Torres                    | 1               |
| Grabadoras de Video Digital \(DVR\)           | 1               |
| Grabadoras de Video en Red \(NVR\)            | 1               |
| Grabadoras Reporteras                         | 1               |
| Grameras                                      | 1               |
| Grapas                                        | 1               |
| Guillotinas                                   | 1               |
| Herramientas para Cables                      | 1               |
| Hidrolavadoras                                | 1               |
| Home Theater                                  | 1               |
| HomePod                                       | 1               |
| Hornos de Microondas                          | 1               |
| Hornos Eléctricos                             | 1               |
| Hubs y Controles Smart                        | 1               |
| Iluminación para Foto y Video                 | 1               |
| Iluminación para PC                           | 1               |
| Iluminadores IR                               | 1               |
| iMac                                          | 1               |
| Impresoras                                    | 1               |
| Impresoras 3D                                 | 1               |
| Impresoras de Cheques                         | 1               |
| Impresoras de Credenciales                    | 1               |
| Impresoras de Etiquetas                       | 1               |
| Impresoras de Matriz de Punto                 | 1               |
| Impresoras de Tickets                         | 1               |
| Impresoras Fotográficas                       | 1               |
| Impresoras Móviles                            | 1               |
| Interfaces de Audio                           | 1               |
| Internal Charges / Products                   | 1               |
| Interruptores Industriales                    | 1               |
| Inversores                                    | 1               |
| iPad                                          | 1               |
| iPad Air                                      | 1               |
| iPad Pro                                      | 1               |
| Jabón                                         | 1               |
| Jacks de Red                                  | 1               |
| Juegos para PC                                | 1               |
| Juegos PlayStation 5                          | 1               |
| Juegos Xbox One                               | 1               |
| Juegos Xbox Series X/S                        | 1               |
| Kits de Alarma                                | 1               |
| Kits de Herramientas                          | 1               |
| Kits de Instalación                           | 1               |
| Kits de Mantenimiento                         | 1               |
| Kits de Micrófonos                            | 1               |
| Kits de Teclado y Mouse                       | 1               |
| Kits de Vigilancia                            | 1               |
| Lámparas                                      | 1               |
| Lámparas para Laptop                          | 1               |
| Lapiceros                                     | 1               |
| Lápices                                       | 2               |
| Lápices para Tabletas                         | 1               |
| Laptops                                       | 1137            |
| Lavadoras                                     | 1               |
| Lectores de Código de Barras                  | 1               |
| Lectores de Huella Digital                    | 1               |
| Lectores de Memoria                           | 2               |
| Lectores de Mostrador                         | 1               |
| LEDs                                          | 1               |
| Lentes                                        | 1               |
| Lentes para Computadora                       | 1               |
| Lentes para Smartphone                        | 1               |
| Licuadoras                                    | 1               |
| Lijadoras y Pulidoras                         | 1               |
| Limpiadores para Electrónicos                 | 1               |
| Linternas                                     | 1               |
| Llaves                                        | 1               |
| Luces Giratorias                              | 1               |
| Luces LED para Interiores                     | 1               |
| Luces Perimetrales                            | 1               |
| Luces Vehiculares                             | 1               |
| Mac Studio                                    | 1               |
| MacBook Air                                   | 14              |
| MacBook Pro                                   | 15              |
| Maletas                                       | 1               |
| Maletines                                     | 1               |
| Maletines para Proyectores                    | 1               |
| Mangueras para Compresores                    | 1               |
| Manos Libres                                  | 1               |
| Máquinas de Coser                             | 1               |
| Máquinas de Sellos                            | 1               |
| Marcadores a Base de Agua                     | 1               |
| Marcadores para Vidrio                        | 1               |
| Marcadores Permanentes                        | 1               |
| Marcadores Punto Fino                         | 1               |
| Martillos y Marros                            | 1               |
| Masajeadores                                  | 1               |
| Memorias Flash                                | 2               |
| Memorias RAM para Laptop                      | 1               |
| Memorias RAM para Mac                         | 1               |
| Memorias RAM para PC                          | 1               |
| Memorias RAM para Servidores                  | 1               |
| Memorias USB                                  | 2               |
| Mesas y Escritorios                           | 1               |
| Mezcladoras                                   | 1               |
| Micas, Cubiertas y Protectores                | 1               |
| Micrófonos                                    | 1               |
| Micrófonos Profesionales                      | 1               |
| Microsoft 365                                 | 1               |
| Microsoft Office                              | 1               |
| Mochilas                                      | 1               |
| Módulos Multifunción                          | 1               |
| Módulos Stack                                 | 1               |
| Módulos Transceptores                         | 1               |
| Módulos y Motores                             | 1               |
| Monitores                                     | 2               |
| Monitores Apple                               | 1               |
| Monitores CCTV                                | 1               |
| Montaje de Redes                              | 1               |
| Montaje para Antenas                          | 1               |
| Montaje para Torres                           | 1               |
| Montajes para Placas de Desarrollo            | 1               |
| Montajes y Cubiertas                          | 1               |
| Mouse                                         | 1               |
| Mouse / Teclados / Trackpads                  | 1               |
| Mousepads                                     | 1               |
| Multicontactos                                | 1               |
| Multifuncionales                              | 1               |
| Navajas                                       | 1               |
| Navegadores GPS                               | 1               |
| No Break                                      | 1               |
| Objetivos Varifocales                         | 1               |
| Ollas y Vaporeras                             | 1               |
| Organizadores de Escritorio                   | 1               |
| Oxímetros                                     | 1               |
| Palas y Picos                                 | 1               |
| Paneles Controladores                         | 1               |
| Paneles de Control                            | 2               |
| Paneles de Control para Alarmas de Incendio   | 1               |
| Paneles Solares                               | 1               |
| Pantallas                                     | 1               |
| Pantallas Comerciales                         | 1               |
| Pantallas de Proyección                       | 1               |
| Pantallas para Placas de Desarrollo           | 1               |
| Pantallas POS Pole                            | 1               |
| Papel                                         | 2               |
| Papel Fotográfico                             | 2               |
| Papel POS                                     | 2               |
| Pararrayos                                    | 1               |
| Parrillas de Gas                              | 1               |
| Parrillas Eléctricas                          | 1               |
| Pasta Térmica                                 | 1               |
| PC's de Escritorio                            | 1               |
| Pedales                                       | 1               |
| Perforadoras                                  | 1               |
| Picos Poncha Llantas                          | 1               |
| Pilas                                         | 1               |
| Pinceles                                      | 1               |
| Pins y Chinches                               | 1               |
| Pinturas                                      | 1               |
| Pinzas                                        | 1               |
| Pistolas de Aire                              | 1               |
| Placas de Desarrollo                          | 1               |
| Planchas                                      | 1               |
| Plotter                                       | 1               |
| Plumones                                      | 1               |
| Podadoras                                     | 1               |
| Polipastos                                    | 1               |
| Porta Mangueras                               | 1               |
| Powerline                                     | 1               |
| Preparación de Alimentos                      | 1               |
| Preparación de Bebidas                        | 1               |
| Presentadores                                 | 1               |
| Procesadores de Alimentos                     | 1               |
| Procesadores para PC                          | 1               |
| Procesadores para Servidores                  | 1               |
| Protección de Mercancia                       | 1               |
| Protectores de Pantalla para iPad             | 1               |
| Protectores de Pantalla para iPhone           | 1               |
| Protectores para Celulares                    | 1               |
| Protectores para PC's                         | 1               |
| Protoboards                                   | 1               |
| Proyectores                                   | 1               |
| Proyectores de Luz                            | 1               |
| Puentes SLI                                   | 1               |
| Puertas de Cortesía y Torniquetes             | 1               |
| Purificadores de Aire                         | 1               |
| Quemadores de Blu-ray                         | 2               |
| Quemadores de DVD                             | 2               |
| Racks Extraíbles y Backplanes                 | 2               |
| Racks y Gabinetes                             | 2               |
| Radios                                        | 1               |
| Radios Despertadores                          | 1               |
| Rasuradoras y Cortadoras                      | 1               |
| Reductores                                    | 1               |
| Reductores de Voltaje                         | 1               |
| Reflectores                                   | 1               |
| Refrigeradores                                | 1               |
| Reguladores de Voltaje                        | 1               |
| Relojes Checadores                            | 1               |
| Repetidores                                   | 1               |
| Repetidores USB                               | 1               |
| Reproductores MP3 / MP4                       | 1               |
| Reproductores para Transmisión Multimedia     | 1               |
| Resina                                        | 1               |
| Respaldos y Utilidades                        | 1               |
| Revisteros                                    | 1               |
| Rodillos de Alimentación                      | 1               |
| Rollos de Papel                               | 1               |
| Rollos de Papel para Plotter                  | 1               |
| Rotomartillos                                 | 1               |
| Router                                        | 2               |
| Routerboards                                  | 1               |
| Sacapuntas                                    | 1               |
| Sartenes y Comales                            | 1               |
| Secadoras                                     | 2               |
| Seguridad para Bebés                          | 1               |
| Selfie Sticks                                 | 1               |
| Sellos, Cojines y Tintas de Sello             | 1               |
| Semáforos y Señalización                      | 1               |
| Sensores                                      | 1               |
| Sensores de Humedad                           | 1               |
| Sensores de Movimiento                        | 1               |
| Separadores                                   | 1               |
| Separadores para Amplificadores               | 1               |
| Servidores                                    | 2               |
| Servidores de Impresión                       | 2               |
| Servidores de Video IP                        | 1               |
| Servidores Seriales                           | 1               |
| Sierras                                       | 1               |
| Sillas                                        | 1               |
| Sillas Gamer                                  | 1               |
| Sirenas y Bocinas                             | 1               |
| Sistemas de Conferencia                       | 1               |
| Sistemas de Grabación                         | 1               |
| Sistemas de Interconexión a la Red Grid - Tie | 1               |
| Sistemas Operativos                           | 1               |
| Sistemas Operativos para Servidores           | 1               |
| Sistemas POS                                  | 1               |
| Smart Plugs                                   | 1               |
| Smartwatch                                    | 2               |
| Sobres                                        | 1               |
| Software para Impresoras                      | 1               |
| Soldadoras                                    | 1               |
| Soldaduras                                    | 1               |
| Sopladoras                                    | 1               |
| Soportes                                      | 1               |
| Soportes para Cámaras                         | 1               |
| Soportes para Celulares y Tabletas            | 2               |
| Soportes para Monitores                       | 1               |
| Soportes para Pantallas                       | 1               |
| Soportes y Accesorios para Montaje            | 2               |
| Soportes y Montajes para Detectores           | 1               |
| Soportes y Paneles                            | 2               |
| SSD                                           | 2               |
| Subwoofers                                    | 1               |
| Sujeción de Canaletas                         | 1               |
| Supresores de Picos                           | 1               |
| Switches                                      | 1               |
| Switches KVM                                  | 2               |
| Tabletas                                      | 4               |
| Tabletas Gráficas                             | 2               |
| Tambores                                      | 1               |
| Tanques de tinta                              | 1               |
| Tapas y Cajas                                 | 1               |
| Tapetes Sanitizantes                          | 1               |
| Tarjetas de Relevador                         | 1               |
| Tarjetas de Televisión                        | 1               |
| Tarjetas de Video                             | 1               |
| Tarjetas Madre                                | 1               |
| Tarjetas para Captura de Video                | 1               |
| Tarjetas para Credenciales                    | 2               |
| Tarjetas para Fuente de Poder                 | 1               |
| Tarjetas PCI                                  | 1               |
| Tarjetas RAID                                 | 1               |
| Tarjetas USB                                  | 1               |
| Tarjetas VoIP                                 | 1               |
| Tarjetas y Módulos                            | 1               |
| Tarjetas y Módulos de Red                     | 1               |
| Tarjetas y Tags de Acceso                     | 1               |
| Teclados                                      | 1               |
| Teclados Numéricos                            | 1               |
| Teclados POS                                  | 1               |
| Teclas para Teclados                          | 1               |
| Teléfonos Alámbricos                          | 1               |
| Teléfonos Inalámbricos                        | 1               |
| Teléfonos VoIP                                | 1               |
| Terminales para Cables                        | 1               |
| Terminales Portátiles                         | 1               |
| Termómetros                                   | 1               |
| Teteras y Hervidoras de Agua                  | 1               |
| Tierra Física                                 | 1               |
| Tintas                                        | 1               |
| Tóner                                         | 1               |
| Tornillos de Banco                            | 1               |
| Toslink                                       | 1               |
| Transceptores y Receptores                    | 1               |
| Transmisores FM                               | 1               |
| Tripies                                       | 1               |
| Unidades de Imagen                            | 1               |
| Unidades de Red Óptica                        | 1               |
| Unidades de Transferencia                     | 1               |
| Unidades Magnéticas                           | 1               |
| Válvulas                                      | 1               |
| Ventiladores                                  | 2               |
| Ventiladores para RAM                         | 1               |
| Videoporteros e Interfones                    | 1               |
| Wattmetros                                    | 1               |
| Webcams                                       | 1               |
| Wi-Fi en Malla                                | 1               |
| Workstations                                  | 23              |




Excercise 4
------------

### Show how many products there are for each brand

    SELECT m.title as Manufacturer, count(a.title) NumberOfProducts
    FROM articles AS a
    JOIN manufacturers AS m ON a.manufacturer_id = m.id
    GROUP BY m.title;

The selection specifies the columns to be returned. It selects the title from the manufacturers table (aliased as m) and renames it as Manufacturer. It also counts the number of title entries from the articles table (aliased as a) and labels this count as NumberOfProducts. It also specifies the articles table as the primary source of data and aliases it as a. 

Then, a join is made between the articles table and the manufacturers table (aliased as m). The join is made on the condition that the manufacturer_id column in the articles table matches the id column in the manufacturers table. This links each article to its respective manufacturer.

Finally, it groups the results by the manufacturer's title. The grouping is necessary because the query includes an aggregate function (COUNT). It ensures that the count of articles is calculated separately for each manufacturer.


**Results:**

| Manufacturer | NumberOfProducts |
| :--- | :--- |
| ABB | 2 |
| ACCESSPRO | 5 |
| ACCO | 2 |
| ACER | 66 |
| ACTECK | 3 |
| ACTIVISION | 1 |
| ADATA | 3 |
| AEROCOOL | 2 |
| AJAX | 1 |
| ALCTRON | 1 |
| ALIEN | 2 |
| ALIENWARE | 8 |
| ALLIED TELESIS | 2 |
| ALPHACOOL | 1 |
| ALTRONIX | 1 |
| AMAZON | 1 |
| AMD | 1 |
| AMERICAN | 1 |
| ANCLO | 1 |
| ANTROLITE | 4 |
| AORUS | 4 |
| APPLE | 43 |
| ARUBA | 1 |
| ASSA ABLOY | 2 |
| ASTRON | 1 |
| ASUS | 121 |
| ATL | 2 |
| AUDIOLABS | 1 |
| AZOR | 3 |
| BALAMRUSH | 2 |
| BEA | 1 |
| BEEPER | 2 |
| BEHRINGER | 2 |
| BELDEN | 1 |
| BENQ | 1 |
| BESTEK | 1 |
| BINDEN | 5 |
| BIRD TECHNOLOGIES | 2 |
| BIXOLON | 1 |
| BLACK & DECKER | 4 |
| BLECK | 1 |
| BOSCH | 1 |
| BOWER | 2 |
| BROBOTIX | 5 |
| BROTHER | 5 |
| BUFFALO | 1 |
| CABLEMOD | 1 |
| CANON | 2 |
| CASE LOGIC | 1 |
| CELICA | 1 |
| CENTURY | 1 |
| CHAROFIL | 1 |
| CHEFMAN | 1 |
| CHOETECH | 1 |
| CINSA | 1 |
| CISCO | 1 |
| COMMSCOPE | 2 |
| CONAIR | 1 |
| COOLER MASTER | 1 |
| CORSAIR | 3 |
| CREALITY | 4 |
| CYBERPOWER | 1 |
| D-LINK | 2 |
| DAHUA | 11 |
| DATAPAC | 1 |
| DATAPRODUCTS | 1 |
| DEEPCOOL | 1 |
| DELL | 184 |
| DERWENT | 3 |
| DKS DOORKING | 1 |
| DYNABOOK | 4 |
| EC LINE | 2 |
| EKCO | 1 |
| ELECTRONIC ARTS | 1 |
| ELGATO | 2 |
| ELO TOUCHSYSTEMS | 1 |
| ENERGIZER | 3 |
| ENSON | 1 |
| EPCOM | 15 |
| EPEVER | 1 |
| EPOS | 2 |
| EPSON | 9 |
| ESSELTE | 3 |
| EUROCOLORS | 1 |
| EVGA | 1 |
| EVOLIS | 1 |
| EZVIZ | 1 |
| FELLOWES | 3 |
| FLUKE | 1 |
| FOSET | 1 |
| FOY | 1 |
| FRAGA | 1 |
| FUSSION ACUSTIC | 5 |
| GAMA ITALY | 1 |
| GAME FACTOR | 2 |
| GARMIN | 1 |
| GATEWAY | 7 |
| GBC | 2 |
| GEAR4 | 2 |
| GHIA | 15 |
| GIGABYTE | 12 |
| GOOGLE | 1 |
| GRANDSTREAM | 1 |
| GRIZZLY | 1 |
| HAHNEMUHLE | 1 |
| HAMILTON BEACH | 1 |
| HIKMICRO | 1 |
| HIKVISION | 7 |
| HISENSE | 1 |
| HONEYWELL | 6 |
| HONOR | 2 |
| HP | 298 |
| HP ENTERPRISE | 9 |
| HUAWEI | 11 |
| HYPE | 1 |
| HYPERLUX | 1 |
| HYPERX | 1 |
| HYUNDAI | 19 |
| IFROGZ | 2 |
| IML | 1 |
| IMOU | 1 |
| INDIANA | 1 |
| INTEL | 1 |
| INTELLINET | 2 |
| JABRA | 3 |
| JBL | 1 |
| JENDRIX | 2 |
| KAPTON | 2 |
| KÄRCHER | 1 |
| KASPERSKY | 1 |
| KENSINGTON | 1 |
| KINGSTON | 3 |
| KIWO | 1 |
| KLEIN TOOLS | 1 |
| KOBLENZ | 3 |
| KRO | 1 |
| LANIX | 14 |
| LENOVO | 303 |
| LEXMARK | 2 |
| LG | 5 |
| LINKEDPRO | 6 |
| LINKSYS | 2 |
| LITE-ON | 1 |
| LOGITECH | 5 |
| LUTRON | 1 |
| MAE | 3 |
| MAKITA | 1 |
| MANHATTAN | 9 |
| MASTERCHEF | 1 |
| MAXELL | 1 |
| MEGALUZ | 3 |
| MERIVA TECHNOLOGY | 2 |
| MICROSOFT | 8 |
| MIDEA | 2 |
| MIKROTIK | 1 |
| MIMOSA NETWORKS | 1 |
| MINELAB | 1 |
| MIRATI | 1 |
| MISIK | 1 |
| MODAMOB | 1 |
| MOLOTOW | 4 |
| MOXA | 2 |
| MSI | 37 |
| NATIVE UNION | 2 |
| NECNON | 2 |
| NEXTEP | 3 |
| NINTENDO | 1 |
| Norton LifeLock | 1 |
| OKY | 1 |
| ONKYO | 1 |
| OVALTECH | 1 |
| PANASONIC | 3 |
| PANDUIT | 6 |
| PCTEL | 1 |
| PEAK TOUR | 2 |
| PELIKAN | 1 |
| PERFECT CHOICE | 2 |
| PILOT | 1 |
| PNY | 1 |
| POLITEC | 2 |
| POLY | 4 |
| POSLINE | 2 |
| POWER SONIC | 1 |
| PRECISION | 2 |
| PRETUL | 1 |
| PROLICOM | 1 |
| PROVISION ISR | 2 |
| QIAN | 3 |
| RADOX | 4 |
| RAIDMAX | 1 |
| RASPBERRY | 3 |
| RCI | 1 |
| REMINGTON | 2 |
| RESIDEO | 1 |
| RF INDUSTRIES | 1 |
| RHEEM | 1 |
| RHINO | 1 |
| ROMMS | 1 |
| ROYAL | 2 |
| ROYAL TALENS | 1 |
| SAKURA | 2 |
| SAMSUNG | 4 |
| SANAIRE | 1 |
| SANDISK | 1 |
| SAXXON | 1 |
| SEAGATE | 2 |
| SECO-LARM | 2 |
| SFIRE | 1 |
| SHURE | 1 |
| SL PROLIGHT | 1 |
| SOLAX | 1 |
| SONY | 5 |
| SPARKFUN | 1 |
| StarTech.com | 7 |
| STEEL PRO | 1 |
| STEREN | 14 |
| STI | 1 |
| STYLOS | 1 |
| SURTEK | 6 |
| SYSCOM | 1 |
| TACX | 1 |
| TARGUS | 2 |
| TAURUS | 7 |
| TECHZONE | 1 |
| TECNOLITE | 3 |
| THOMSON | 4 |
| TIMCO | 1 |
| TOTAL GROUND | 1 |
| TOUGHBOOK PANASONIC | 3 |
| TP-LINK | 7 |
| TRAMONTINA | 2 |
| TRIPP LITE | 8 |
| TRUPER | 5 |
| TWELVE SOUTH | 1 |
| TXPRO | 2 |
| UBIQUITI NETWORKS | 6 |
| UGREEN | 2 |
| URREA | 12 |
| VERBATIM | 4 |
| VICA | 1 |
| VICTORINOX | 1 |
| VORAGO | 6 |
| VSG | 1 |
| VSSL | 1 |
| WAVESHARE | 1 |
| WEBOOST | 2 |
| WESTERN DIGITAL | 3 |
| WESTINGHOUSE | 2 |
| WHIRLPOOL | 2 |
| WINLAND | 2 |
| X-MEDIA | 1 |
| XEROX | 6 |
| XIAOMI | 3 |
| XP-PEN | 1 |
| XPG | 6 |
| XSS | 1 |
| XZEAL | 2 |
| YAELTEX | 1 |
| YEALINK | 1 |
| YEASTAR | 1 |
| YLI ELECTRONIC | 1 |
| ZAGG | 1 |
| ZEBRA | 10 |
| ZKTECO | 4 |





Excercise 5
------------

### Show the top 5 most relevant products of each brand

    SELECT m.title AS Manufacturer, a.title as Categories, a.relevance as Relevance
    FROM articles AS a
    JOIN manufacturers AS m ON a.manufacturer_id = m.id
    WHERE (
        SELECT COUNT(*)
        FROM articles AS a2
        WHERE a2.manufacturer_id = a.manufacturer_id AND a2.relevance >= a.relevance
    ) <= 5
    ORDER BY manufacturer, a.relevance DESC;

A selection of three columns from the joined tables is made. It renames m.title to "Manufacturer", a.title to "Categories", and keeps a.relevance as "Relevance".  The data is being fetched from the "articles" table, which is aliased as a to simplify the query and subsequent references.

Then, the "manufacturers" table (aliased as m) are joined. The join condition is that the manufacturer_id field in the articles table matches the id field in the manufacturers table. This join ensures that only articles with a corresponding manufacturer are selected.

The **Where** condition limits the rows to those where the manufacturer has 5 or fewer articles with equal or greater relevance than the current article. It counts the number of articles (COUNT(*)) for the same manufacturer (a2.manufacturer_id = a.manufacturer_id) where the relevance is greater than or equal to (a2.relevance >= a.relevance) the relevance of the current article. If this count is 5 or less, the article is included.

Finally, an **Order By** orders the results first by the manufacturer (alphabetically) and then by the relevance of the articles in descending order (from most relevant to least relevant).

Results:

| Manufacturer        | Categories                                                                                                                                                                                                                                                 | Relevance   |
|:--------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| ABB                 | ABB Relevador de Apertura con Cableado, 240V, para T4/T5/T6                                                                                                                                                                                                | 1.93398     |
| ABB                 | ABB Interruptor Termomagnético 3 Polos 1SDA067435R1, 690V, 125A, Entrada 500V                                                                                                                                                                              | -0.726756   |
| ACCESSPRO           | AccessPRO Detector Fotoeléctrico XBS-RR7, 7 Metros                                                                                                                                                                                                         | 1.64081     |
| ACCESSPRO           | AccessPro Torniquete Bidireccional AP5000HD, 98cm, Acero Inoxidable                                                                                                                                                                                        | 1.22406     |
| ACCESSPRO           | AccessPRO Brazo Articulado para Barreras XBS-4M-RA/XBS-4M-LA, 4 Metros                                                                                                                                                                                     | 0.641507    |
| ACCESSPRO           | AccessPRO Semáforo Peatonal con Movimiento Verde/Rojo PROLIGHTPASD                                                                                                                                                                                         | 0.636684    |
| ACCESSPRO           | AccessPro Picos Poncha LLantas para Barrera Vehicular XB-TK-1M, 100cm, Amarillo                                                                                                                                                                            | -0.726446   |
| ACCO                | Acco Separador 442, 5 Divisiones, Blanco                                                                                                                                                                                                                   | 0.284969    |
| ACCO                | Acco Foliador Royall de 7 Dígitos RNM7A-7, Negro                                                                                                                                                                                                           | -1.39574    |
| ACER                | Laptop Acer Aspire 3 14" Full HD, Intel Core i5-1135G7 2.40GHz, 8GB, 512GB SSD, Windows 11 Home 64-bit, Español, Plata                                                                                                                                     | 11.7332     |
| ACER                | Laptop Acer Aspire 3 A315-56 15.6" Full HD, Intel Core i3-1005G1 1.20GHz, 8GB, 512GB SSD, Windows 11 Home 64-bit, Negro                                                                                                                                    | 2.82858     |
| ACER                | Laptop Acer Aspire 5 A514-54-55ZZ 14" HD, Intel Core i5-1135G7 2.40GHz, 8GB, 1TB + 256GB SSD, Windows 11 Home 64-bit, Español, Plata                                                                                                                       | 2.75667     |
| ACER                | Laptop Acer Aspire 3 15.6" Full HD, Intel Core i3-1115G4 3GHz, 8GB, 256GB SSD, Windows 11 Home 64-Bit, Ingles, Plata                                                                                                                                       | 2.75594     |
| ACER                | Laptop Acer Aspire 5 A515-54-77JE 15.6" Full HD, Intel Core i7-10510U 1.80GHz, 8GB, 512GB SSD, Windows 11 Home 64-bit, Español, Negro                                                                                                                      | 2.35247     |
| ACTECK              | Acteck Smartwatch Motion Sport SW250, Touch, Bluetooth 5.0, Android/iOS, Negro - Resistente a Salpicaduras y Polvo                                                                                                                                         | 13.0018     |
| ACTECK              | Acteck Adaptador Divisor Splitter de Audífonos, 3.5mm Hembra - 2x 3.5mm Macho, Negro                                                                                                                                                                       | 12.2125     |
| ACTECK              | Acteck Lector de Memoria DH450, MicroSD, USB A/C, Negro                                                                                                                                                                                                    | 2.17268     |
| ACTIVISION          | Call of Duty WWII Gold Edition, Xbox One ― Producto Digital Descargable                                                                                                                                                                                    | 0.412626    |
| ADATA               | Adata Gabinete de Disco Duro ED600 2.5'', SATA III, USB 3.1, Negro                                                                                                                                                                                         | 13.7943     |
| ADATA               | Cargador Portátil Adata P10000QCD, 10.000mAh, Blanco                                                                                                                                                                                                       | 12.7597     |
| ADATA               | Memoria USB Adata UR340, 128GB, USB 3.2, Lectura 100 MB/s, Negro                                                                                                                                                                                           | 11.7823     |
| AEROCOOL            | Aerocool Mirage L240 Enfriamiento Líquido para CPU, 2x 120mm, 600 - 1800RPM, Rosa                                                                                                                                                                          | 12.7966     |
| AEROCOOL            | Ventilador Aerocool Air Frost Plus LED RGB, 124mm, 1500RPM, Negro                                                                                                                                                                                          | 12.4546     |
| AJAX                | AJAX Detector de Ruptura de Vidrio GlassProtect, Inalámbrico, hasta 9 Metros, Blanco                                                                                                                                                                       | 0.230105    |
| ALCTRON             | Alctron Interfaz de Audio USB XU-2 MKII, USB, XLR, Negro                                                                                                                                                                                                   | 10.7659     |
| ALIEN               | Alien Luces LED Blanco, 5 Metros - incluye 1 Cable de Energía                                                                                                                                                                                              | 11.2933     |
| ALIEN               | Alien Bafle Profesional Amplificador SP 15, 15", Inalámbrico/Alámbrico, 2x XL6.3mm, Bluetooth, 500W RMS, Negro                                                                                                                                             | 0.522354    |
| ALIENWARE           | Laptop Gamer Alienware M15 R7 15.6" Full HD, Intel Core i7-12700H 3.50GHz, 16GB, 512GB SSD, NVIDIA GeForce RTX 3060, Windows 11 Home 64-bit, Español, Negro                                                                                                | 10.7074     |
| ALIENWARE           | Laptop Gamer Alienware M15 15.6" Full HD, AMD Ryzen 7 6800H 3.2GHz, 16GB, 512GB SSD, NVIDIA GeForce RTX 3050 Ti, Windows 11 Home 64-bit, Español, Negro                                                                                                    | 2.94639     |
| ALIENWARE           | Laptop Gamer Alienware M15 R4 15.6" Full HD, Intel Core i7-10870H 2.20GHz, 16GB, 512GB SSD, NVIDIA GeForce RTX 3060, Windows 10 Home 64-bit, Negro \(2021\) ― Garantía Limitada por 1 Año                                                                  | 1.00204     |
| ALIENWARE           | Laptop Gamer Alienware X17 R2 17.3" Full HD, Intel Core i7-12700H 2.30GHz, 16GB, 512GB SSD, NVIDIA GeForce RTX 3060, Windows 11 Home 64-bit, Español, Blanco                                                                                               | 0.284669    |
| ALIENWARE           | Laptop Gamer Alienware M15 R7 15.6" Full HD, Intel Core i7-12700H 2.30GHz, 16GB, 1TB, NVIDIA GeForce RTX 3070 Ti, Windows 11 Home 64-bit, Español, Negro                                                                                                   | 0.279098    |
| ALLIED TELESIS      | Allied Telesis Módulo Transceptor MiniGbic AT-SPLX10A SFP, LC Monomodo, 1000 Mbit/s, 10Km, 1310nm                                                                                                                                                          | 9.89879     |
| ALLIED TELESIS      | Allied Telesis Convertidor de Medios Gigabit Ethernet a Fibra Óptica SC Multimodo, 100Mbit/s, 2000 Metros                                                                                                                                                  | 0.581552    |
| ALPHACOOL           | Alphacool Placa de Respaldo GPX Eisblock, LED, para NVIDIA RTX 2080/RTX 2080 Ti/RTX 2070                                                                                                                                                                   | -0.539397   |
| ALTRONIX            | Altronix Tarjeta de Control de Alimentación ACM8, Entrada 12 - 24V, 8 salidas AC                                                                                                                                                                           | -0.232554   |
| AMAZON              | Amazon Kit de Echo Dot Asistentes de Voz 3ra Generación, Inalámbrico, WiFi, Bluetooth, 2 Piezas                                                                                                                                                            | 13.2161     |
| AMD                 | Procesador AMD Ryzen 5 3600, S-AM4, 3.60GHz, 32MB L3 Cache, con Disipador Wraith Stealth                                                                                                                                                                   | 15.078      |
| AMERICAN            | American Batidora de Mano 9975, 120W, 7 Velocidades, Blanco/Gris                                                                                                                                                                                           | 12.3647     |
| ANCLO               | Anclo Tubo Flexible Galvanizado 1'', 30 Metros, Plata                                                                                                                                                                                                      | 9.822       |
| ANTROLITE           | Antrolite Radio Análogo Portátil Midland 75, 40 Canales, Negro                                                                                                                                                                                             | 11.6012     |
| ANTROLITE           | Antrolite Soporte para Tableta 6”-12”, Negro                                                                                                                                                                                                               | 11.2746     |
| ANTROLITE           | Antrolite Slipmats UC Neon, 2 Piezas, Naranja/Plata                                                                                                                                                                                                        | 10.9203     |
| ANTROLITE           | Antrolite Estrobo EST001, 45W, Rojo                                                                                                                                                                                                                        | 10.8846     |
| AORUS               | Laptop AORUS 15 XE4 15.6” Full HD, Intel Core i7-12700H  2.30GHz, 16GB, 1TB SSD, NVIDIA GeForce RTX 3070 Ti, Windows 11 Home 64-bit, Español, Negro                                                                                                        | 0.878443    |
| AORUS               | Laptop Gamer AORUS 5 SE4 15.6" Full HD, Intel Core i7-12700H 3.50GHz, 16GB, 512GB SSD, NVIDIA GeForce RTX 3070, Windows 11 Home 64-bit, Español, Negro                                                                                                     | 0.852459    |
| AORUS               | Laptop Gamer AORUS 5 KE4 15.6" Full HD, Intel Core i7-12700H 3.50GHz, 16GB, 1TB SSD, NVIDIA GeForce RTX 3060, Windows 11 Home 64-bit, Español, Negro                                                                                                       | -99.0732    |
| AORUS               | Laptop AORUS 15 XE4 15.6” Quad HD, Intel Core i7-12700H  2.30GHz, 16GB, 1TB SSD, NVIDIA GeForce RTX 3070 Ti, Windows 11 Home 64-bit, Español, Negro                                                                                                        | -99.7691    |
| APPLE               | Apple AirPods \(2da. Generación\), Inalámbrico, Bluetooth, Blanco - incluye Estuche de Carga Alámbrico                                                                                                                                                     | 13.5093     |
| APPLE               | Apple iMac Retina 24", Apple M1, 8GB, 256GB SSD, Azul \(Abril 2021\)                                                                                                                                                                                       | 12.7845     |
| APPLE               | Apple iPad Air 5 Retina 10.9", 64GB, WiFi, Blanco Estelar \(5.ª Generación - Marzo 2022\)                                                                                                                                                                  | 11.9312     |
| APPLE               | Apple Teclado Magic MQ052E/A, Bluetooth, Blanco \(Español\)                                                                                                                                                                                                | 11.5254     |
| APPLE               | Apple iPad 9 Retina 10.2", 64GB, WiFi, Plata \(9.ª Generación - Septiembre 2021\)                                                                                                                                                                          | 11.4841     |
| ARUBA               | Aruba Cable R9D20A SFP+ Macho - SFP+ Macho, 3 Metro, Negro/Plata                                                                                                                                                                                           | 0.613215    |
| ASSA ABLOY          | Assa Abloy Smart Hub para Cerraduras, Inalámbrico, WiFi, Blanco                                                                                                                                                                                            | 9.39804     |
| ASSA ABLOY          | Assa Abloy Manija Modular Eifel Tampa 26 D, Metálico                                                                                                                                                                                                       | -0.932704   |
| ASTRON              | Astron Fuente de Poder Conmutada SS-12, Entrada 100 - 240V, Salida 13,8V, 12A                                                                                                                                                                              | 1.46007     |
| ASUS                | Gabinete ASUS ROG Z11 con Ventana, Mini-Tower, Mini-DTX/Mini-ITX, USB 2.0/3.2, sin Fuente, sin Ventiladores Instalados, Negro                                                                                                                              | 14.311      |
| ASUS                | Laptop ASUS ProArt Studiobook Pro 16 16" WQXGA, AMD Ryzen 9 5900HX 3.30GHz, 32GB, 1TB SSD, NVIDIA RTX A2000, Windows 11 Pro 64-bit, Español, Negro                                                                                                         | 12.3334     |
| ASUS                | Mousepad ASUS NC12 TUF GAMING P1 DS, 36 x 26cm, Grosor 3mm, Demon Slayer L.E. Nezuko Kamado                                                                                                                                                                | 11.4536     |
| ASUS                | Laptop ASUS ExpertBook B1400 14" Full HD, Intel Core i5-1135G7 2.40GHz, 8GB, 512GB SSD, Windows 10 Pro 64-bit, Español, Negro                                                                                                                              | 10.5837     |
| ASUS                | Laptop ASUS ExpertBook B1400CEAE 14" Full HD, Intel Core i5-1135G7 2.40GHz, 8GB, 1TB HDD, Windows 10 Pro 64-bit, Español, Negro                                                                                                                            | 2.75592     |
| ATL                 | ATL Set de Pastillas Acuarelas para Arte con Pincel G101, 12 Colores                                                                                                                                                                                       | 1.42677     |
| ATL                 | ATL Marco de Madera, 40 x 50cm, sin Tela                                                                                                                                                                                                                   | 1.3552      |
| AUDIOLABS           | Audiolabs Amplificador para Auto ADL-C1100.1D, 1 Canal, 2000W RMS, Negro                                                                                                                                                                                   | 10.7644     |
| AZOR                | Azor Carpeta Arillo Redondo, 4'', para 800 Hojas de Tamaño Carta, Negro                                                                                                                                                                                    | 1.16358     |
| AZOR                | Azor Sacapuntas Manual 305-A, Azul/Amarillo                                                                                                                                                                                                                | -1.39567    |
| AZOR                | Azor Marcador Aquarelo Glass para Vidrio/Cartulina/Papel, Punto Extra Grande, Blanco                                                                                                                                                                       | -1.43538    |
| BALAMRUSH           | Balam Rush Escritorio Gamer Olympus MRX3000, 100 x 64cm, Negro                                                                                                                                                                                             | 13.3543     |
| BALAMRUSH           | Tapete Gamer Balam Rush ULTIMATE, 12 x 12cm, Grosor 5mm, Negro/Rojo                                                                                                                                                                                        | 10.3493     |
| BEA                 | Bea Sensor de Microondas 10FALCON, Ángulo de 0 - 180°                                                                                                                                                                                                      | 2.52325     |
| BEEPER              | Beeper Bocinas para Auto BOC-40218, 250W, 2 Vías, 90dB, 4", Negro                                                                                                                                                                                          | 12.1991     |
| BEEPER              | Beeper Desarmador de Bola y Puntas, 6 Piezas, Negro                                                                                                                                                                                                        | 10.6933     |
| BEHRINGER           | Behringer Pedal Digital DR600, Negro/Plata                                                                                                                                                                                                                 | 10.3992     |
| BEHRINGER           | Behringer Sistema de Grabación PODCASTUDIO 2 USB, incluye Micrófono, Audífonos y Mezclador Premium                                                                                                                                                         | -0.285168   |
| BELDEN              | Belden Panel de Parcheo Cat6 KeyConnect, 1U, 24 Puertos, Negro                                                                                                                                                                                             | 9.60584     |
| BENQ                | BenQ Kit Adaptador Inalámbrico para Proyector InstaShow WDC10, HDMI, Negro                                                                                                                                                                                 | 9.62441     |
| BESTEK              | Bestek Inversor de Corriente MRZ3011HU, 300W, Entrada 15V, Salida 120V,  2 Contactos                                                                                                                                                                       | 1.96348     |
| BINDEN              | Binden Batería BAT-DM107, 900mAh, para Drone DM107S                                                                                                                                                                                                        | 11.4382     |
| BINDEN              | Binden Kit de Lentes 10 en 1 Universal, para Smartphone                                                                                                                                                                                                    | 10.9646     |
| BINDEN              | Binden Gatillo Falcon F5, Alámbrico, USB, Negro                                                                                                                                                                                                            | 10.9448     |
| BINDEN              | Binden Manos Libres K10, Bluetooth, Inalámbrico, Negro                                                                                                                                                                                                     | 10.2833     |
| BINDEN              | Drone Binden B19 con Cámara 4K, 4 Rotores, hasta 600 Metros, Blanco                                                                                                                                                                                        | 1.87334     |
| BIRD TECHNOLOGIES   | Bird Technologies Wattmetro 4230-006-1, Gris                                                                                                                                                                                                               | 0.0597276   |
| BIRD TECHNOLOGIES   | Bird Technologies Elemento de 100W, 25 - 60MHz, para BIRD 43                                                                                                                                                                                               | 0.0597276   |
| BIXOLON             | Bixolon Pantalla POS Pole BCD-2000, USB 2.0, Negro                                                                                                                                                                                                         | -0.929962   |
| BLACK & DECKER      | Black & Decker Plancha de Vapor Seco, Antiadherente, 0.25 Litros, Rojo/Blanco                                                                                                                                                                              | 13.8096     |
| BLACK & DECKER      | Black & Decker Combo 2 Sartenes, Licuadora y Batidora de Pedestal, Rojo                                                                                                                                                                                    | 13.203      |
| BLACK & DECKER      | Black & Decker Sierra Caladora KS501, 420W, Naranja                                                                                                                                                                                                        | 2.59509     |
| BLACK & DECKER      | Black & Decker Desbrozadora GL300 B3, 350W, 23cm, Naranja                                                                                                                                                                                                  | 1.54277     |
| BLECK               | Bleck Banda Extensible para Smartband, Azul                                                                                                                                                                                                                | 1.99414     |
| BOSCH               | Bosch Tarjeta de Proximidad RFID, 8.5 x 5.4cm, Blanco, 25 Piezas                                                                                                                                                                                           | 11.2152     |
| BOWER               | Bower Kit Filtro para Cámara Ultravioleta Polarizado, 3 Filtros, Negro - incluye Estuche                                                                                                                                                                   | 10.9107     |
| BOWER               | Bower Kit Cámara SFD06 6 en 1 para Flash                                                                                                                                                                                                                   | -0.252518   |
| BROBOTIX            | BRobotix Base Enfriadora para Laptop 17", con Ventilador de 1400RPM, Negro/Blanco                                                                                                                                                                          | 10.9716     |
| BROBOTIX            | BRobotix Adaptador Tipo Jack 3.5mm, Negro/Verde                                                                                                                                                                                                            | 8.69727     |
| BROBOTIX            | BRobotix Soporte para PC 6001301, hasta 23.5cm, Negro                                                                                                                                                                                                      | 0.625083    |
| BROBOTIX            | BRobotix Cable FireWire Macho - FireWire Macho, 3 Metros, Negro                                                                                                                                                                                            | 0.323933    |
| BROBOTIX            | Brobotix Tarjeta PCI Express Serial DB9, 2 Puertos x RS-232                                                                                                                                                                                                | 0.0334847   |
| BROTHER             | Tóner Brother TN-750 Negro, 8000 Páginas                                                                                                                                                                                                                   | 13.6716     |
| BROTHER             | Tambor Brother DR620, 25.000 Páginas                                                                                                                                                                                                                       | 11.6576     |
| BROTHER             | Brother ST371HD Máquina de Coser, 37 Puntadas, 1 Paso ― Incluye Kit de Aseo y Caja de Hilos                                                                                                                                                                | 2.59493     |
| BROTHER             | Brother Repuesto para Entintar Sello PRINKB, Negro                                                                                                                                                                                                         | -0.992331   |
| BROTHER             | Brother Máquina de Sellos SC-2000USB, 600 x 600 DPI, USB, Windows                                                                                                                                                                                          | -1.43677    |
| BUFFALO             | Buffalo BRXL-PT6U2VB, Grabador de Blu-ray Portátil, BD-R 6x / DVD+R 8x / CD-RW 16x, Externo, Negro                                                                                                                                                         | 10.2175     |
| CABLEMOD            | Cablemod Kit de Cables de Poder PCI Express, Blanco, incluye 1x Cable ATX 24-pin/1x EPS 8-pin/1x EPS 4+4-pin/1xPCI-E 16-pin a 3x8-pin                                                                                                                      | 2.85247     |
| CANON               | Cámara Réflex Canon EOS Rebel T7, 24.1MP, Cuerpo + Lente EF-S 18-55mm IS II                                                                                                                                                                                | 10.3869     |
| CANON               | Canon Kit Cabezal para Pixma G1100/G2100/G3100/G4100                                                                                                                                                                                                       | 2.10998     |
| CASE LOGIC          | Case Logic Estuche para Cámara Digital, Negro                                                                                                                                                                                                              | 1.64141     |
| CELICA              | Celica Calculadora Científica FX-82MS, 10+2 Dígitos, Batería/Energía Solar, Negro                                                                                                                                                                          | 1.20433     |
| CENTURY             | Century Tag para Ropa T005, Blanco, 100 Piezas                                                                                                                                                                                                             | -0.727857   |
| CHAROFIL            | Charofil Ménsula Omega Tipo L Inteligente, 31cm, Metal                                                                                                                                                                                                     | 11.406      |
| CHEFMAN             | Chefman Freidora de Aire Turbo Fry, 7.5 Litros, Negro/Acero Inoxidable                                                                                                                                                                                     | 11.0693     |
| CHOETECH            | Choetech Cargador Inalámbrico de Carga Rápida T559-F, 15W, Negro                                                                                                                                                                                           | 12.1803     |
| CINSA               | Cinsa Batería de Cocina Yubicela, Acero Vitrificado, Antiadherente, 4 Piezas, Blanco                                                                                                                                                                       | -0.1162     |
| CISCO               | Cisco Módulo FlexStack-Plus para Switch Catalyst 2960-X                                                                                                                                                                                                    | -101.323    |
| COMMSCOPE           | Commscope Jack Cat6, RJ-45, Blanco                                                                                                                                                                                                                         | 10.515      |
| COMMSCOPE           | CommScope Kit de Montaje Punta Torre, Plata                                                                                                                                                                                                                | 0.261544    |
| CONAIR              | Conair Tina masajeador para Pies FB5XBCRES, Rosa/Blanco                                                                                                                                                                                                    | 13.511      |
| COOLER MASTER       | Cooler Master Disipador para VGA Hydra 8800, para NVIDIA GeForce 8800GTX/Ultra, 1800RPM                                                                                                                                                                    | -1.43678    |
| CORSAIR             | Corsair Panel de Vidrio Templado AIRFLOW para iCUE 4000X/4000D/4000D, Blanco                                                                                                                                                                               | 2.85229     |
| CORSAIR             | Memoria RAM Corsair DDR3, 1066MHz, 4GB, CL7, SO-DIMM, para Mac                                                                                                                                                                                             | 1.3496      |
| CORSAIR             | Corsair Base para Audífonos ST50, Negro                                                                                                                                                                                                                    | 1.03489     |
| CREALITY            | Creality Impresora 3D Ender-3 V2, 22 x 22 x 25cm, Negro                                                                                                                                                                                                    | 2.59951     |
| CREALITY            | Creality Bobina de Filamento CR-ABS, 1.75mm, 1Kg, Azul                                                                                                                                                                                                     | 1.80335     |
| CREALITY            | Creality Resina para Impresora 3D 3302020027, Rígida Estándar, 1Kg, Blanco                                                                                                                                                                                 | 1.80318     |
| CREALITY            | Creality Conectores Neumáticos con Abrazaderas, Azul/Plata/Dorado                                                                                                                                                                                          | 1.2452      |
| CYBERPOWER          | CyberPower Transformador Reductor OL5KSTF, Entrada 208V, Salida 120V                                                                                                                                                                                       | 1.09511     |
| D-LINK              | D-Link Cable Switch KVM KVM-222, USB+VGA, 1.8 Metros, 2 Puertos                                                                                                                                                                                            | 10.2514     |
| D-LINK              | D-Link Cámara PT para Bebé DCS-850L Lite, Inalámbrico                                                                                                                                                                                                      | -1.39593    |
| DAHUA               | Dahua Monitor LED 22”para Videovigilancia, HDMI/VGA, 1920 x 1080 Pixeles, Negro                                                                                                                                                                            | 13.3086     |
| DAHUA               | Dahua Kit Videoportero KTW01, Monitor 7", Altavoz, Inalámbrico/Alámbrico, Negro/Blanco                                                                                                                                                                     | 12.2097     |
| DAHUA               | Dahua Cable Coaxial BNC/DC Macho - BNC Macho/DC Hembra, 30 Metros, Negro                                                                                                                                                                                   | 11.6422     |
| DAHUA               | Dahua Módulo de Control de Acceso ASC2102B-T, 2 Puertas, 20.000 Usuarios, Negro                                                                                                                                                                            | 10.9327     |
| DAHUA               | Dahua Cámara CCTV Domo IR para Interiores/Exteriores HAC-HDBW2501RN-Z, Antivandálica, Alámbrico, 2592 x 1944 Pixeles, Día/Noche                                                                                                                            | 10.8981     |
| DATAPAC             | Cinta Datapac DP-031 Negro                                                                                                                                                                                                                                 | 9.62092     |
| DATAPRODUCTS        | DataProducts Impresora 2600, Blanco y Negro, Matriz de Puntos, 360 x 360 DPI, USB, Negro                                                                                                                                                                   | -0.726986   |
| DEEPCOOL            | Disipador CPU DeepCool AK620, 120mm, 500-1850RPM, Negro                                                                                                                                                                                                    | 13.3595     |
| DELL                | Monitor Dell E2016HV LED 19.5'', Negro                                                                                                                                                                                                                     | 17.5915     |
| DELL                | Laptop Dell Latitude 3420 14" HD, Intel Core i5-1135G7 2.40GHz, 8GB, 256GB SSD, Windows 10 Pro 64-bit, Español, Negro                                                                                                                                      | 11.7885     |
| DELL                | Laptop Dell Vostro 3405 14" HD, AMD Ryzen 5 3450U 2.10GHz, 8GB, 256GB, Windows 11 Pro 64-bit, Español, Negro                                                                                                                                               | 10.901      |
| DELL                | Laptop Dell Inspiron 3511 15.6" Full HD, Intel Core i7-1165G7 2.80GHz, 8GB, 256GB SSD, Windows 11 Home 64-bit, Español, Azul                                                                                                                               | 10.5045     |
| DELL                | Laptop Dell Latitude 5430 14" Full HD, Intel Core i7-1255U 4.70GHz Turbo, 16GB, 512GB SSD, Windows 11 Pro 64-bit, Español, Gris                                                                                                                            | 9.95411     |
| DERWENT             | Derwent Colores, Caja Metálica, 12 Lápices                                                                                                                                                                                                                 | 0.0730104   |
| DERWENT             | Derwent Lápiz de Dibujo, Caja Metálica con 6 Piezas                                                                                                                                                                                                        | 0.0677339   |
| DERWENT             | Derwent Lápiz de Grafito, Caja Metálica con 12 Piezas                                                                                                                                                                                                      | 0.0646077   |
| DKS DOORKING        | DKS Doorking Barrera Vehicular 1601-380, hasta 4 Metros - no Incluye Mástil                                                                                                                                                                                | 1.65156     |
| DYNABOOK            | Laptop Dynabook Satellite Pro C40-H 14" HD, Intel Core i3-1005G1 1.20GHz, 4GB, 256GB SSD, Windows 10 Home 64-bit, Español, Azul                                                                                                                            | -0.101176   |
| DYNABOOK            | Laptop Dynabook Tecra A40-J 14" Full HD, Intel Core i5-1135G7 2.40GHz, 8GB, 512GB SSD, Windows 10 Pro 64-bit, Español, Azul ― incluye 3 Años de Garantía en Sitio                                                                                          | -0.101186   |
| DYNABOOK            | Laptop Dynabook Satellite Pro C40-H 14" HD, Intel Core i5-1035G1 1GHz, 8GB, 512GB SSD, Windows 10 Home 64-bit, Español, Azul                                                                                                                               | -0.101206   |
| DYNABOOK            | Laptop Dynabook Satellite Pro C50-H15100 15.6" HD, Intel Core i3-1005G1 1.20GHz, 4GB, 128GB SSD, Windows 10 Home 64-bit, Inglés, Azul                                                                                                                      | -0.158425   |
| EC LINE             | EC Line EC-PM-58110, Kit Impresora de Tickets, Térmica Directa, USB, Negro - incluye Lector de Código de Barras                                                                                                                                            | 13.1961     |
| EC LINE             | Cajón de Dinero EC Line EC-CD-50M con Llave, 5kg, Negro                                                                                                                                                                                                    | 11.9431     |
| EKCO                | Ekco Cacerola, 16cm, Esmalte Vitrificado, Azul                                                                                                                                                                                                             | 11.2192     |
| ELECTRONIC ARTS     | FIFA 23, Xbox Series X                                                                                                                                                                                                                                     | 1.03484     |
| ELGATO              | Elgato Brazo para Cámaras e Iluminación Master Mount S, Negro                                                                                                                                                                                              | 0.183557    |
| ELGATO              | Elgato Tarjeta de Captura de Video Digital Cam Link Pro, 4K, 4x HDMI, PCIe                                                                                                                                                                                 | 0.122513    |
| ELO TOUCHSYSTEMS    | Elo TouchSystems Sistema POS E484291 17”, Intel Core i3-8100T 3.10GHz, 4GB, 128GB SSD,  Windows 10 Home                                                                                                                                                    | 0.448531    |
| ENERGIZER           | Energizer Pilas No-Recargables AA, 1.5V, 8 Piezas                                                                                                                                                                                                          | 13.8755     |
| ENERGIZER           | Energizer Linterna LED Tipo Pluma LINENEPLED23AE, 35 Lúmenes, Metálico                                                                                                                                                                                     | 13.3714     |
| ENERGIZER           | Energizer Lámpara LED de Escritorio LINENEBOOK, 14 Lúmenes, Flexible, con Clip, Gris                                                                                                                                                                       | 11.6505     |
| ENSON               | Enson Gabinete Metálico LINCE10 para Proteger Sirena de 15W                                                                                                                                                                                                | 9.37557     |
| EPCOM               | Epcom Barra de Luz Ultra Brillante LED 40.6" para Exteriores XD200F, Blanca                                                                                                                                                                                | 10.9425     |
| EPCOM               | Epcom Receptor de Video, Cat5e/6, 120/150 Metros, para Kit Matricial TT-683-Matrix                                                                                                                                                                         | 10.619      |
| EPCOM               | Epcom Adaptador de Microfonos para Cámaras IP, Negro                                                                                                                                                                                                       | 10.0921     |
| EPCOM               | Epcom Receptor Pasivo de Video EPMON255R, RJ-45 Hembra, Azul                                                                                                                                                                                               | 9.84626     |
| EPCOM               | Epcom Luz Auxiliar Trasera, 300 Lúmenes, Negro/Naranja para Bicicleta                                                                                                                                                                                      | 2.21267     |
| EPEVER              | EPEVER Controlador de Carga Solar XTRA 3415N, 12 - 48V, 30A                                                                                                                                                                                                | 0.583082    |
| EPOS                | EPOS Cable para Auricular CSTD 08, Negro                                                                                                                                                                                                                   | 0.220225    |
| EPOS                | EPOS Dispositivo para Descolgar HSL 10 II, Negro                                                                                                                                                                                                           | -0.0785562  |
| EPSON               | Epson EcoTank L1210, Color, Inyección, Tanque de Tinta, Alámbrico, Print                                                                                                                                                                                   | 13.7162     |
| EPSON               | Plotter Epson SureColor T3170 24'', Color, Inyección, Print                                                                                                                                                                                                | 13.652      |
| EPSON               | Tanque de Tinta Epson T673, 70ml, 6 Piezas                                                                                                                                                                                                                 | 12.8489     |
| EPSON               | Epson TM-U295, Impresora de Cheques, Alámbrico, Serial, Blanco - Sin Cables ni Fuente de Poder                                                                                                                                                             | 12.2018     |
| EPSON               | Epson Papel de Presentación Mate Ultra Premium , 13'' x 19'', 100 Hojas                                                                                                                                                                                    | 8.99251     |
| ESSELTE             | Esselte Caja de Cartón para Archivo Deslizable con Gaveta, 65x43x29cm, Blanco                                                                                                                                                                              | 1.29553     |
| ESSELTE             | Esselte Sobre Coin 75007, Paquete de 500 Piezas, 8.9 x 16.5cm, Color Manila                                                                                                                                                                                | 0.664934    |
| ESSELTE             | Esselte Archivo Expandible Portadocumento F068BK, Cierre Elástico, Tamaño Oficio, 13 Divisiones, Negro                                                                                                                                                     | -1.43629    |
| EUROCOLORS          | Eurocolors Fólder PU0003, Paquete de 25 Piezas, Tamaño Carta, Surtido Neón                                                                                                                                                                                 | 0.0536356   |
| EVGA                | EVGA PRO SLI Bridge HB de 4 Slots, 120mm                                                                                                                                                                                                                   | -1.26113    |
| EVOLIS              | Evolis PM2-0025-A Impresora de Tarjetas, Transferencia Térmica, 300 x 1200 DPI, USB, Ethernet, Negro/Blanco                                                                                                                                                | 2.17101     |
| EZVIZ               | Ezviz Contacto Magnético WiFi T2C para Puerta/Ventana, Interiores, Inalámbrico, Blanco                                                                                                                                                                     | 2.85393     |
| FELLOWES            | Fellowes Engargoladora Star+ 150, hasta 150 Hojas, Gris                                                                                                                                                                                                    | 9.00256     |
| FELLOWES            | Fellowes Trituradora de Corte Cruzado Powershred 12C, 12 Hojas, 19 Litros, Negro                                                                                                                                                                           | 0.168693    |
| FELLOWES            | Fellowes Encuadernadora Helios 60, 600 Hojas                                                                                                                                                                                                               | -1.19073    |
| FLUKE               | Fluke Termómetro IR 62 MAX, -30 - 500°C                                                                                                                                                                                                                    | 10.9506     |
| FOSET               | Foset Filtro de Agua PURA-P3, Blanco - Elimina 99.99% de Bacterias                                                                                                                                                                                         | -0.326517   |
| FOY                 | Foy Disco para Sierra 143565, 14", 60 Dientes, para Madera/Madera Laminada/PVC                                                                                                                                                                             | 1.61319     |
| FRAGA               | Fraga Parrilla de Gas P502, 2 Quemadores, Negro                                                                                                                                                                                                            | 11.0111     |
| FUSSION ACUSTIC     | Fussion Acustic Foco LED Bluetooth con Bocina Integrada LDB-0009, RGB, Base E27, Blanco                                                                                                                                                                    | 12.1045     |
| FUSSION ACUSTIC     | Fussion Acustic Aro de Luz LED con Tripie, Negro                                                                                                                                                                                                           | 11.5924     |
| FUSSION ACUSTIC     | Fussion Acustic Cargador de Pilas AA/AAA - incluye 4 Pilas AA                                                                                                                                                                                              | 11.403      |
| FUSSION ACUSTIC     | Fussion Acustic Adaptador VGA Hembra - Mini MAC Macho, Blanco                                                                                                                                                                                              | 10.762      |
| FUSSION ACUSTIC     | Fussion Acustic Transmisor FM para Auto RF-1511WH, USB-A, Negro/Blanco                                                                                                                                                                                     | 1.80245     |
| GAMA ITALY          | Gama Italy Depiladora Oasis Supreme, 8 Pasos, 2 Velocidades, Rosa/Blanco                                                                                                                                                                                   | 1.25591     |
| GAME FACTOR         | Game Factor Lentes Anti-Radiación para Computadora GG301, Unisex, Azul                                                                                                                                                                                     | 11.1067     |
| GAME FACTOR         | Game Factor Pasta Térmica TP300, -250 - 350 °C, 2 Gramos                                                                                                                                                                                                   | 10.8143     |
| GARMIN              | Garmin Navegador GPS eTrex 32x, 2.2", USB, Negro/Gris                                                                                                                                                                                                      | 10.5998     |
| GATEWAY             | Laptop Gateway GWTN116-3 11.6" HD, Intel Celeron N4020 1.10GHz, 4GB, 64GB eMMC, Windows 10 Home S 64-bit, Inglés, Azul                                                                                                                                     | 0.287767    |
| GATEWAY             | Laptop Gateway GWTN116-3 11.6" HD, Intel Celeron N4020 1.10GHz, 4GB, 64GB eMMC, Windows 10 Home S 64-bit, Inglés, Verde                                                                                                                                    | 0.287657    |
| GATEWAY             | Laptop Gateway Ultra Slim 14.1" Full HD, Intel Core i3-1005G1 1.20GHz, 4GB, 128GB SSD, Windows 10 Home S 64-bit, Inglés, Negro                                                                                                                             | 0.0662171   |
| GATEWAY             | Laptop Gateway GWTN116-3 11.6" HD, Intel Celeron N4020 1.10GHz, 4GB, 64GB eMMC, Windows 10 Home S 64-bit, Inglés, Azul                                                                                                                                     | -99.2718    |
| GATEWAY             | Laptop Gateway GWTN116-3 11.6" HD, Intel Celeron N4020 1.10GHz, 4GB, 64GB eMMC, Windows 10 Home S 64-bit, Inglés, Rojo                                                                                                                                     | -99.6793    |
| GBC                 | GBC Cubiertas GBPlak, Paquete de 50 Piezas, Tamaño Carta, Verde                                                                                                                                                                                            | 9.37781     |
| GBC                 | GBC Guillotina Classiccut Lite de 12'', hasta 10 Hojas                                                                                                                                                                                                     | 1.16322     |
| GEAR4               | Gear4 Funda Crystal Palace Clear para iPhone 7/8/SE, Transparente                                                                                                                                                                                          | 1.54298     |
| GEAR4               | Gear4 Correa Trenzada para Apple Watch 41/40/38mm, Talla M, Negro                                                                                                                                                                                          | 0.948821    |
| GHIA                | Regulador Ghia GVR-010, 400W, 1000VA, Entrada 120V, Salida 120V, 4 Contactos                                                                                                                                                                               | 11.0771     |
| GHIA                | Ghia 2 en 1 Only Due Pro 10.1" HD, Intel Celeron J3355 2GHz, 3GB, 64GB eMMC, Windows 10 Pro 64-bit, Español, Gris                                                                                                                                          | 10.9838     |
| GHIA                | Ghia 2 en 1 ShiftPro 11.6" HD, Intel Celeron N4000 1.10GHz, 4GB, 64GB eMMC, Windows 10 Pro 64-bit, Español, Negro                                                                                                                                          | 10.6269     |
| GHIA                | Laptop Ghia Libero 14.1" HD, Intel Celeron J3355 2GHz, 4GB, 128GB eMMC, Windows 10 Pro 64-bit, Español, Negro                                                                                                                                              | 1.98182     |
| GHIA                | Celular Ghia GQWERTY 2.31”, Doble Sim, Bluetooth, Negro/Rojo                                                                                                                                                                                               | 0.141404    |
| GIGABYTE            | Tarjeta Madre Gigabyte Micro ATX B560M DS3H V2, S-1200, Intel B560 Express, HDMI, 128GB DDR4 para Intel                                                                                                                                                    | 15.1835     |
| GIGABYTE            | Laptop Gamer Gigabyte AERO 5 XE4 15.6" 4K Ultra HD, Intel Core i7-12700H 2.30GHz, 16GB, 1TB SSD, NVIDIA GeForce RTX 3070 Ti, Windows 11 Home  64-bit, Español, Negro                                                                                       | 2.81777     |
| GIGABYTE            | Laptop Gigabyte U4 UD 14" Full HD, Intel Core i5-1155G7 2.50GHz, 16GB, 512GB, Windows 11 Home, Inglés, Gris ― incluye Impresora                                                                                                                            | 2.35224     |
| GIGABYTE            | Laptop Gigabyte U4 UD 14" Full HD, Intel Core i5-1155G7 2.50GHz, 16GB, 512GB, Windows 11 Home, Inglés, Gris ― incluye Mouse Gamer Aorus/Configuración Especial, 1 Año de Garantía                                                                          | 1.05976     |
| GIGABYTE            | Laptop Gigabyte U4 UD 14" Full HD, Intel Core i5-1155G7 2.50GHz, 16GB, 512GB, Windows 11 Home, Inglés, Gris ― incluye Quemador LG/Hub Vorago/Configuración Especial, 1 Año de Garantía                                                                     | 1.05976     |
| GOOGLE              | Google Chromecast Gen 3, Full HD, WiFi, HDMI, Negro \(Inglés\)                                                                                                                                                                                             | 12.2565     |
| GRANDSTREAM         | Grandstream ATA HT814, 4 Puertos FXS, 2x RJ-45                                                                                                                                                                                                             | 11.993      |
| GRIZZLY             | Computadora Gamer Grizzly Draknosh, AMD Ryzen 7 Pro 4750G 3.60GHz, 16GB, 1TB + 500GB SSD, NVIDIA GeForce RTX 3060, Windows 10 Prueba                                                                                                                       | 13.7671     |
| HAHNEMUHLE          | Hahnemühle Cuaderno Sketch Diary Black, A5, 14.8 x 21cm, 60 Hojas, Negro, para Escribir                                                                                                                                                                    | 10.9027     |
| HAMILTON BEACH      | Hamilton Beach Chocomilera DrinkMaster, 0.8 Litros, 2 Velocidades, Negro                                                                                                                                                                                   | 10.3932     |
| HIKMICRO            | Hikmicro Cámara Térmica Portátil Pocket 2 3.5", 4x Zoom, WiFi, Negro                                                                                                                                                                                       | 1.99421     |
| HIKVISION           | Hikvision Kit de Vigilancia HK-1080-CV de 4 Cámaras CCTV Bullet ColorVu y 4 Canales, con Fuente de Poder y Accesorios de Instalación                                                                                                                       | 12.4757     |
| HIKVISION           | Hikvision Kit Sensor de Movimiento PIR de Montaje en Pared DS-PDP15P-EG2-WB, Inalámbrico, Anti-Pet, hasta 15 Metros, Blanco, incluye Control Remoto DS-PKF1-WB, 2 Sensores de Movimiento DS-PDP15P-EG2-WB, 3 Contactos Magnéticos DS-PDMCS-EG2-WB y 1 Sire | 11.8613     |
| HIKVISION           | Hikvision Kit DVR de 4 Canales Turbo HD ColorVu DS-7104HGHI-K1 para 1 Disco Duro, máx. 4TB, 2x USB 2.0, 1x RJ-45, incluye 4 Cámaras CCTV DS-2CE10DF0T-F, 4 Cables Coaxiles y Fuente de Poder                                                               | 10.9438     |
| HIKVISION           | Hikvision Detector de Humo DS-PDSMK-S-WB, Inalámbrico, Blanco                                                                                                                                                                                              | 10.3931     |
| HIKVISION           | Hikvision Kit de Montaje para Cerradura Electromagnetica, para DS-K4H258S                                                                                                                                                                                  | 1.89451     |
| HISENSE             | Hisense Congelador FC50D6AWX1, 142L, 5 Pies Cúbicos, Blanco                                                                                                                                                                                                | 2.86838     |
| HONEYWELL           | Honeywell HF680-R1-2USB Lector de Código de Barras 2D - incluye Cables                                                                                                                                                                                     | 12.7247     |
| HONEYWELL           | Honeywell Solaris 7980g Lector de Código de Barras 1D/2D - incluye Cable USB                                                                                                                                                                               | 12.5141     |
| HONEYWELL           | Honeywell Terminal Portátil EDA71 7", 2GB, Android, Bluetooth                                                                                                                                                                                              | 11.2352     |
| HONEYWELL           | Honeywell Kit de Alarma VISTA48/6150TB, incluye Teclado/Transformador/Batería/Gabinete                                                                                                                                                                     | 10.9808     |
| HONEYWELL           | Honeywell Batería 318-063-002, Li-Ion, 5200mAh, Negro, para CK65                                                                                                                                                                                           | 10.9619     |
| HONOR               | Laptop Honor MagicBook 14 14" HD, Intel Core i5-1135G7 2.40GHz, 8GB, 512GB SSD, Windows 10 Home 64-bit, Español, Plata                                                                                                                                     | -0.390274   |
| HONOR               | Laptop Honor MagicBook 15 15.6" Full HD, AMD Ryzen 5 3500U 2.10GHz, 16GB, 512GB SSD, Windows 10 Home 64-bit, Inglés, Gris Mate                                                                                                                             | -99.4697    |
| HP                  | Laptop HP 245 G8 14" HD, AMD Ryzen 3 3250 2.60GHz, 8GB, 256GB SSD, Windows 11 Home 64-bit, Español, Plata                                                                                                                                                  | 13.3607     |
| HP                  | Laptop HP ZBook Firefly 15 G8 15.6" Full HD, Intel Core i7-1165G7 2.80GHz, 16GB, 512GB SSD, NVIDIA Quadro T500, Windows 10 Pro 64-bit, Español, Plata                                                                                                      | 13.3259     |
| HP                  | Laptop HP ProBook 450 G9 15.6" HD, Intel Core i5-1235U 1.30GHz, 8GB, 512GB SSD, NVIDIA GeForce MX570, Windows 11 Pro 64-bit, Español, Plata                                                                                                                | 13.1742     |
| HP                  | Multifuncional HP Ink Tank 315, Color, Inyección de Tinta Térmica, Tanque de Tinta, Alámbrico, Print/Scan/Copy                                                                                                                                             | 13.1527     |
| HP                  | Laptop HP 240 G8 14" HD, Intel Core i3-1115G4 1.70GHz, 8GB, 512GB SSD, Windows 11 Pro 64-bit, Español, Negro                                                                                                                                               | 13.0506     |
| HP ENTERPRISE       | Disco Duro para Servidor HPE 801882-B21 RAW 3.5'', 1TB, SATA III, 6 Gbit/s, 7200 RPM, Cache                                                                                                                                                                | 13.0014     |
| HP ENTERPRISE       | Servidor HPE ProLiant MicroServer Gen10+, Intel Xeon E-2224 3.40GHz, 16GB DDR4, 1TB, máx. 16TB, 3.5", SATA, Ultra Micro Tower - no Sistema Operativo Instalado                                                                                             | 12.6011     |
| HP ENTERPRISE       | HPE StoreEasy 1660 SAS de 8 Bahías, 32TB, Intel Xeon Bronze 3204 1.90GHz, RJ-45, Negro ― Incluye Discos Duros                                                                                                                                              | 10.0939     |
| HP ENTERPRISE       | HPE Microsoft Windows Server 2022 Standard ROK, 16-Core, 64-bit, 1 Licencia                                                                                                                                                                                | 10.0338     |
| HP ENTERPRISE       | HP Enterprise Adaptador de Corriente R3K00A, Entrada 100 - 240V, Salida 12V, para Access Point AP-505                                                                                                                                                      | 2.05222     |
| HUAWEI              | Laptop Huawei MateBook D14 14" Full HD, Intel Core i7-1165G7 2.80GHz, 16GB, 512GB SSD, Windows 10 Pro 64-bit, Español, Gris                                                                                                                                | 11.1439     |
| HUAWEI              | Laptop Huawei MateBook 14s 14.2" Full HD, Intel Core i7-11370H 3.3GHz, 16GB, 512GB SSD, Windows 10 Home 64-bit, Español, Gris                                                                                                                              | 0.494345    |
| HUAWEI              | Laptop Huawei MateBook D14 14" Full HD, AMD Ryzen 5 5500U 2.10GHz, 8GB, 512GB SSD, Windows 10 Home 64-bit, Español, Plata                                                                                                                                  | 0.104056    |
| HUAWEI              | Laptop Huawei MateBook B3-420 14" Full HD, Intel Core i5-1135G7 2.40GHz, 8GB, 512GB SSD, Windows 10 Pro 64-bit, Gris Espacial                                                                                                                              | -0.00853136 |
| HUAWEI              | Laptop Huawei MateBook B3-510 15.6" Full HD, Intel Core i3-10110U 1.60GHz, 8GB, 256GB SSD, Windows 10 Pro 64-bit, Español, Gris                                                                                                                            | -0.0309273  |
| HYPE                | Proyector Portátil Hype M24 3LCD, 800x480, máx. 1200 Lúmenes, con Bocinas, Amarillo                                                                                                                                                                        | 12.8428     |
| HYPERLUX            | Hiperlux Iluminador Infrarrojo 90°, hasta 45 Metros, Beige                                                                                                                                                                                                 | 9.39793     |
| HYPERX              | HyperX Set de 19 Piezas Rubber, Rosa                                                                                                                                                                                                                       | 1.35224     |
| HYUNDAI             | Laptop Hyundai HyBook N4020 14.1", Intel Celeron N4020 1.10GHz, 4GB, 128GB, Windows 10 Home S, Gris ― Incluye Tablet HyTab Plus 8WB1, Mouse y Maletín                                                                                                      | 2.21423     |
| HYUNDAI             | Laptop Hyundai Hybook 14.1" HD, Intel Celeron N3350 1.10GHz, 4GB, 64GB, Windows 10 Home 64-bit, Inglés, Gris                                                                                                                                               | 1.85025     |
| HYUNDAI             | Laptop Hyundai HyBook 14.1" HD, Intel Celeron N3350 1.10GHz, 4GB, 1TB + 64GB eMMC, Windows 10 Home S 64-bit, Inglés, Negro                                                                                                                                 | 1.77987     |
| HYUNDAI             | Laptop Hyundai HyBook 14.1" HD, Intel Celeron N3350 1.10GHz, 4GB, 1TB + 64GB eMMC, Windows 10 Home 64-bit, Español, Gris Espacial                                                                                                                          | 1.77986     |
| HYUNDAI             | Laptop Hyundai 2 en 1 HyFlip 14" Full HD, Intel Celeron N3350 1.10GHz, 4GB, 64GB HDD, Windows 10 Home 64-bit, Español, Gris                                                                                                                                | 1.77894     |
| IFROGZ              | Ifrogz Mica de Cristal Protectora para iPhone 13/13 Pro/14                                                                                                                                                                                                 | 2.21449     |
| IFROGZ              | iFrogz Protector de Pantalla Glassguard para iPhone X, Transparente                                                                                                                                                                                        | 0.217509    |
| IML                 | IML Antena para Televisión Yagui ABC40R, Exterior, UHF/VHF/HDTV, Aluminio                                                                                                                                                                                  | 11.5897     |
| IMOU                | Imou Cámara IP Smart WiFi Domo IR para Interiores Ranger 2C, Inalámbrico, 1920 x 1080 Pixeles, Día/Noche - Incluye Cámara Imou Cue WiFi                                                                                                                    | 12.784      |
| INDIANA             | Indiana Cable de Cobre para Instalación de Pararrayos, 1/0 AWG, 19 Hilos, 15 Metros, Negro                                                                                                                                                                 | 0.622513    |
| INTEL               | Intel NUC Kit NUC7PJYHN, Intel Pentium Silver J5005 1.50GHz \(Barebone\) - Incluye Cable de Alimentación                                                                                                                                                   | 10.7337     |
| INTELLINET          | Intellinet Bote para Plug RJ-45 Cat5e UTP Sólido, Transparente, 100 Piezas                                                                                                                                                                                 | 12.5383     |
| INTELLINET          | Intellinet Probador de Cables de Red, RJ-11/RJ-45, 4 LEDs                                                                                                                                                                                                  | 10.2507     |
| JABRA               | Jabra Sistema de Videoconferencia PanaCast, 4K Ultra HD 180°, 1x USB-C, Negro                                                                                                                                                                              | 13.4564     |
| JABRA               | Jabra Altavoz SPEAK 510+ MS, Inalámbrico/Alámbrico, USB/Bluetooth, Negro, con Jabra Link 370                                                                                                                                                               | 12.2271     |
| JABRA               | Jabra Cable Adaptador Link 265, USB Macho - 2x QD, Negro                                                                                                                                                                                                   | 9.23121     |
| JBL                 | JBL Subwoofer Stage3 8627, 50W RMS, 65 - 20.000Hz, 6 x 8”, Negro                                                                                                                                                                                           | 11.4156     |
| JENDRIX             | Jendrix Pinza de Compresión PY-107, F/BNC/RG-58/RG-59, Rojo/Negro                                                                                                                                                                                          | 10.9145     |
| JENDRIX             | Jendrix Cautín tipo Lápiz de Lujo SD-102, 30W, Negro                                                                                                                                                                                                       | 0.604006    |
| KAPTON              | Kapton Cable Extensión Speakon Macho - Speakon Macho, 7.5  Metros, Negro                                                                                                                                                                                   | 11.5619     |
| KAPTON              | Kapton Ecualizador Gráfico CR-231EQ, 31 Bandas, Púrpura/Negro                                                                                                                                                                                              | 10.6621     |
| KÄRCHER             | Karcher Hidrolavadora a Presión K2 Classic, 1600psi, Amarillo                                                                                                                                                                                              | 10.9594     |
| KASPERSKY           | Kaspersky Anti-Virus 2017, 1 Usuario, 1 Año, Windows                                                                                                                                                                                                       | 9.89685     |
| KENSINGTON          | Kensington Filtro de Privacidad MagPro Elite para MacBook Pro 16", Negro                                                                                                                                                                                   | 2.75598     |
| KINGSTON            | Memoria RAM Kingston DDR4, 2666MHz, 32GB, Non-ECC, CL19, SO-DIMM                                                                                                                                                                                           | 14.0477     |
| KINGSTON            | Memoria Flash Kingston Canvas Select Plus, 128GB MicroSDXC UHS-I Clase 10, con Adaptador                                                                                                                                                                   | 12.8964     |
| KINGSTON            | Kingston Rieles de Montaje para Desktop a 3.5'' con Soporte y Tornillos                                                                                                                                                                                    | 1.36692     |
| KIWO                | KIWO Mini Home Theater AAHTD20, Bluetooth, Alámbrico, 2 Canales, 30W RMS, Negro, CD Player Incluido                                                                                                                                                        | 0.573765    |
| KLEIN TOOLS         | Klein Tools Grapas con Aislamiento 450-003, 9 x 15mm, para Cables NM \(Romex\) 14/3/14/3G/12/3/Cables de 11/32''/19/32''                                                                                                                                   | 0.0262805   |
| KOBLENZ             | Koblenz Aspiradora Seco-Mojado WD-6 L212, 22.7 Litros, Negro/Azul                                                                                                                                                                                          | 13.2638     |
| KOBLENZ             | Koblenz Supresor de Picos SS-550 USB, 5x NEMA 5–15R, 2x USB, 550 Joules, Gris                                                                                                                                                                              | 10.068      |
| KOBLENZ             | Koblenz Secadora de Carga Vertical SCK-55, 5.5kg, Blanco                                                                                                                                                                                                   | 2.19528     |
| KRO                 | KronalinE Rollo de Papel para Impresora de Inyección de Tinta, N2", 75g/m², 35.8" x 164'                                                                                                                                                                   | 1.65478     |
| LANIX               | Laptop Lanix Neuron X Pro 41298 14" Full HD, Intel Core i5-1135G7 2.40GHz, 8GB, 512GB SSD, Windows 10 64-bit, Español, Negro                                                                                                                               | 2.39355     |
| LANIX               | Laptop Lanix Neuron V 15.6" Full HD, Intel Core i5-10210U 1.6GHz, 8GB, 512GB SSD, Windows 11 Home, Español, Negro                                                                                                                                          | 2.25616     |
| LANIX               | Laptop Lanix Neuron V v7 15.6" Full HD, Intel Core i5-10210U 1.60GHz, 8GB, 512GB SSD, Windows 10 Home 64-bit, Español, Negro                                                                                                                               | 0.878473    |
| LANIX               | Laptop Lanix Neuron V V7 15.6" Full HD, Intel Core i5-10210U 1.60GHz, 8GB, 512GB SSD, Windows 10 Pro 64-bit, Español, Negro                                                                                                                                | 0.463695    |
| LANIX               | Laptop Lanix Neuron AL V12 14" HD, Intel Celeron N4020 1.10GHz, 4GB, 128GB SSD, Windows 10 Home 64-bit, Español, Plata                                                                                                                                     | 0.396467    |
| LENOVO              | Memoria RAM Lenovo 4ZC7A08709 DDR4, 2933MHz, 32GB                                                                                                                                                                                                          | 16.2542     |
| LENOVO              | Laptop Gamer Lenovo Legion 5 15ITH6 15.6" Full HD, Intel Core i5-11400H 2.70GHz, 16GB, 512GB SSD, NVIDIA GeForce RTX 3050, Windows 11 Home 64-bits, Español, Azul/Negro                                                                                    | 15.3039     |
| LENOVO              | Laptop Lenovo ThinkPad L14 G1 14" HD, AMD Ryzen 3 4300U 2.70GHz, 8GB, 256GB SSD, Windows 10 Pro 64-bit, Español, Negro                                                                                                                                     | 14.684      |
| LENOVO              | Laptop Lenovo ThinkBook 14-IIL 14" Full HD, Intel Core i3-1005G1 1.20GHz, 8GB, 1TB, Windows 10 Pro 64-bit, Español, Gris                                                                                                                                   | 14.391      |
| LENOVO              | Memoria RAM Lenovo DDR4, 2933MHz, 64GB, ECC, CL21                                                                                                                                                                                                          | 14.3838     |
| LEXMARK             | Lexmark Fotoconductor 72K0P00, 175.000 Páginas                                                                                                                                                                                                             | 1.45264     |
| LEXMARK             | Lexmark Unidad de Imagen 50F0Z00, 60.000 Páginas                                                                                                                                                                                                           | 1.21865     |
| LG                  | LG Bocina Portátil XBOOM Go XG5, Bluetooth, Alámbrico/Inalámbrico, 20W RMS, USB C, Negro - Resistente al Agua                                                                                                                                              | 13.1285     |
| LG                  | LG Smart TV LED UHD AI ThinQ UQ80 55", 4K Ultra HD, Negro                                                                                                                                                                                                  | 11.9735     |
| LG                  | LG CK43 Mini Componente, Bluetooth, 300W RMS, USB 2.0, Negro                                                                                                                                                                                               | 10.6913     |
| LG                  | LG Aire Acondicionado Minisplit VM182CL, 18000 BTU/h, Blanco                                                                                                                                                                                               | 2.52633     |
| LG                  | LG Barra de Sonido S40Q, Bluetooth, Inalámbico, 2.1 Canales, 300W RMS, Negro                                                                                                                                                                               | 1.77882     |
| LINKEDPRO           | LinkedPRO Bobina de Cable Cat5e para Exterior, 305 Metros, Negro                                                                                                                                                                                           | 12.3957     |
| LINKEDPRO           | LinkedPRO Rack Abierto de 4 Postes 19", 45U, hasta 900kg, Negro                                                                                                                                                                                            | 10.7753     |
| LINKEDPRO           | LinkedPRO Cable de Fibra Óptica para Exteriores de 12 Hilos, Monomodo, Negro - Precio por Metro                                                                                                                                                            | 2.8572      |
| LINKEDPRO           | LinkedPRO Charola para Rack 1U, hasta 110Kg, Negro                                                                                                                                                                                                         | 2.85338     |
| LINKEDPRO           | LinkedPRO Panel de Carriles para Rack 19", Negro - 2 Piezas                                                                                                                                                                                                | 2.37457     |
| LINKSYS             | Router Linksys con Sistema de Red Wi-Fi en Malla MX10600, 2402Mbps, 2.4/5/5GHz,  Antena Interna - 2 Piezas ― ¡Compre más de $1,999 en productos Linksys y participe en el sorteo de 1 Router WHW0101!                                                      | 14.5142     |
| LINKSYS             | Access Point Linksys de Banda Dual AX3600, 2400 Mbit/s, 2x RJ-45,  2.4/5GHz, 8 Antenas de 5.19dBi ― ¡Compre más de $1,999 en productos Linksys y participe en el sorteo de 1 Router WHW0101!                                                               | 13.8026     |
| LITE-ON             | Lite-On iHAS124 Quemador de DVD, DVD-R 24x / DVD+RW 8x, Interno, SATA, Negro \(Bulk\)                                                                                                                                                                      | 11.9548     |
| LOGITECH            | Mouse Logitech Óptico Pebble M350, Inalámbrico, Bluetooth, 1000DPI, Blanco                                                                                                                                                                                 | 17.0244     |
| LOGITECH            | Kit de Teclado y Mouse Logitech MK200, USB, Negro \(Español\)                                                                                                                                                                                              | 12.7867     |
| LOGITECH            | Logitech Lápiz Digital para iPad, Plata                                                                                                                                                                                                                    | 11.3635     |
| LOGITECH            | Logitech Kit Volante Driving Force G29, Alámbrico, USB 2.0, para PC/PlayStation 3/4                                                                                                                                                                        | 9.74771     |
| LOGITECH            | Logitech Presentador R500S, Inalámbrico, USB, Grafito                                                                                                                                                                                                      | 3.32866     |
| LUTRON              | Lutron Hub Repetidor de Señal Inalámbrico, Blanco                                                                                                                                                                                                          | -0.726746   |
| MAE                 | Mae Organizador Giratorio de Escritorio OGE-20, Negro                                                                                                                                                                                                      | 1.30449     |
| MAE                 | MAE Cutter Metálico Chico, 24 Piezas, Gris                                                                                                                                                                                                                 | -0.568472   |
| MAE                 | Mae Tachuela PVC, Paquete de 100 Piezas, Blanco                                                                                                                                                                                                            | -1.39025    |
| MAKITA              | Makita Brocasierra Bimetálica D-21783, 3-5/8”                                                                                                                                                                                                              | 11.3058     |
| MANHATTAN           | Manhattan Convertidor HDMI Macho - VGA Hembra, Negro                                                                                                                                                                                                       | 12.9472     |
| MANHATTAN           | Manhattan Adaptador USB A - Serial RS-232, 0.45 Metros, Transparente                                                                                                                                                                                       | 12.379      |
| MANHATTAN           | Manhattan Cable USB A Macho - USB A Hembra, 10 Metros, Negro                                                                                                                                                                                               | 12.1219     |
| MANHATTAN           | Manhattan Adaptador USB-C 3.1 Macho - DVI Hembra, Negro                                                                                                                                                                                                    | 9.60902     |
| MANHATTAN           | Manhattan Cable para Monitor SVGA 8mm, HD15 Macho - HD15 Hembra, 4.5 Metros, Negro                                                                                                                                                                         | 9.50307     |
| MASTERCHEF          | MasterChef Molino de Granos de Café y Especias MKCG1SP, 150W, Acero Inoxidable                                                                                                                                                                             | 11.9123     |
| MAXELL              | Maxell Cartucho de Limpieza HS-4 DDS, 4mm                                                                                                                                                                                                                  | -1.2305     |
| MEGALUZ             | Proyector de Luz Contour 30, 1 Pieza                                                                                                                                                                                                                       | 11.84       |
| MEGALUZ             | Megaluz Luces Giratorias MARS BEAM, LED RGB, Negro                                                                                                                                                                                                         | 10.9545     |
| MEGALUZ             | Megaluz Mezcladora PMX1260D, 12 Canales, Bluetooth, XLR, Oro                                                                                                                                                                                               | 1.23369     |
| MERIVA TECHNOLOGY   | Meriva Technology Cable BNC Macho - BNC Macho, 18 Metros, Negro                                                                                                                                                                                            | 1.16786     |
| MERIVA TECHNOLOGY   | Meriva Technology Bandeja para Disco Duro SATA 2.5", para MDVR MX1-HDG3G                                                                                                                                                                                   | 0.168423    |
| MICROSOFT           | Microsoft 365 Familia, 5 Dispositivos, 6 Usuarios, 1 Año, Español, Windows/Mac/Android/iOS                                                                                                                                                                 | 13.0875     |
| MICROSOFT           | Microsoft Windows 11 Pro Español, 64-bit, 1 Usuario, OEM                                                                                                                                                                                                   | 11.2246     |
| MICROSOFT           | Microsoft Office Hogar y Empresas 2021, 1 Usuario, para Windows/Mac                                                                                                                                                                                        | 11.0108     |
| MICROSOFT           | Xbox Live Gold, 1 Año ― Producto Digital Descargable                                                                                                                                                                                                       | 10.7034     |
| MICROSOFT           | Microsoft Control para Xbox Series X/S/One Robot White, Inalámbrico, Bluetooth, Blanco                                                                                                                                                                     | 10.1377     |
| MIDEA               | Midea Horno de Microondas MMDF07S2BW, 0.7 Pies Cúbicos, 1050W, 20 Litros, Blanco/Negro                                                                                                                                                                     | 11.0438     |
| MIDEA               | Midea Lavadora de Carga Vertical MLTS101M2SGDW, 10.1Kg, Negro/Blanco                                                                                                                                                                                       | 10.2775     |
| MIKROTIK            | MikroTik RouteBoard RB912UAG-5HPND, 300 Mbit/s, 1x RJ-45, 5GHz                                                                                                                                                                                             | -0.726886   |
| MIMOSA NETWORKS     | Mimosa Networks Radio de Backhaul Modular C5X, 8dBi, 4.9 - 6.4GHz - Requiere Adaptador PoE, se Vende por Separado                                                                                                                                          | 11.3644     |
| MINELAB             | Minelab Detector de Metal Portátil Go Find 11, Sonido Ajustable                                                                                                                                                                                            | 1.85221     |
| MIRATI              | Mirati Smart Plug MCI2, WiFi, 1 Conector, 1100W, 10A, Blanco                                                                                                                                                                                               | 12.1706     |
| MISIK               | Misik Radio Despertador MR420, AM/FM, Negro                                                                                                                                                                                                                | 10.5403     |
| MODAMOB             | Modamob Silla Canis, Respaldo de Rejilla, Negro                                                                                                                                                                                                            | 0.833941    |
| MOLOTOW             | Molotow Plumon Grafx Art, Maskin Liquido, 4mm                                                                                                                                                                                                              | 0.442428    |
| MOLOTOW             | Molotow Set de Marcador Acrílico One4All 227HS Basic 1, 6 Piezas, 4mm, Rellenable, Negro/Azul/Naranja/Rojo/Blanco/Amarillo                                                                                                                                 | 0.129564    |
| MOLOTOW             | Molotow Marcador Permanente 760PI, 60mm, Negro                                                                                                                                                                                                             | 0.122863    |
| MOLOTOW             | Molotow Válvula 900077, 1.5cm, Azul                                                                                                                                                                                                                        | -99.4779    |
| MOXA                | Moxa Servidor Serial TCC-100, 1x RS-232/422/485 DB9, Negro                                                                                                                                                                                                 | 12.5722     |
| MOXA                | Moxa Montaje DK35A para Montaje en Riel DIN, Verde                                                                                                                                                                                                         | 0.604006    |
| MSI                 | Laptop Gamer MSI GP66 Leopard 11UG-688 15.6" Full HD, Intel Core i7-11800H 2.30GHz, 16GB, 1TB SSD, NVIDIA GeForce RTX 3070, Windows 11 Home 64-bit, Negro                                                                                                  | 12.2278     |
| MSI                 | Laptop Gamer MSI GF63 Thin 11UC-1073MX 15.6" Full HD, Intel Core i5-11400H 2.70GHz, 8GB, 512GB SSD, GeForce RTX 3050, Windows 11 Home 64-bit, Español, Negro                                                                                               | 1.49472     |
| MSI                 | Laptop Gamer MSI Sword 15 A12UE 15.6" Full HD, Intel Core i7-12700H 1.70GHz, 16GB, 512GB SSD, NVIDIA GeForce RTX 3060, Windows 11 Home 64-bit, Español, Blanco                                                                                             | 1.32728     |
| MSI                 | Laptop Gamer MSI Sword 15 A12UC 15.6" Full HD, Intel Core i5-12500H 1.30GHz, 16GB, 512GB SSD, NVIDIA GeForce RTX 3050, Windows 11 Home 64-bit, Español, Blanco                                                                                             | 1.32728     |
| MSI                 | Laptop Gamer MSI Bravo 15 B5DD-090MX 15.6" Full HD, AMD Ryzen 5 5600H 3.30GHz, 16GB, 512GB SSD, AMD Radeon RX 5500M, Windows 11 Home 64-bit, Español, Negro                                                                                                | 1.32703     |
| NATIVE UNION        | Native Union Cable RCA de 4 Pares 8x RCA Macho - 8x RCA Macho, 3 Metros                                                                                                                                                                                    | 2.75589     |
| NATIVE UNION        | Native Union Funda para AirPods 3ra Gen., Negro                                                                                                                                                                                                            | 0.878713    |
| NECNON              | Cámara Digital Infantil para Niños NCD-KIDSCAM, 8MP, Azul/Amarillo - Resistente a Impactos                                                                                                                                                                 | 10.734      |
| NECNON              | Tablero Arcade Necnon NCA-6084 Fights, 6084 Juegos, Multicolor                                                                                                                                                                                             | 1.96342     |
| NEXTEP              | Nextep Perforadora de 2 Orificios NE-121M, hasta 20 Hojas, 8cm, Negro                                                                                                                                                                                      | 0.622216    |
| NEXTEP              | Nextep Cesto para Basura de Malla Redondo NE-165RP, 16 Litros, Plata                                                                                                                                                                                       | 0.00618042  |
| NEXTEP              | Nextep Revistero de Metal NE-163A, 6 Ranuras, 2 Bandejas, Negro                                                                                                                                                                                            | -0.714686   |
| NINTENDO            | Nintendo Switch OLED, 64GB, Wi-Fi, Neón                                                                                                                                                                                                                    | 0.0452139   |
| Norton LifeLock     | Norton Utilities Ultimate, 1 Usuario, 10 Dispositivos, 1 Año, Windows ― Producto Digital Descargable                                                                                                                                                       | 0.437564    |
| OKY                 | OKY Pinza Robótica OS-06016, 2° Libertad, Aluminio                                                                                                                                                                                                         | 10.5253     |
| ONKYO               | Onkyo Receptor AV TX-NR7100 para Home Cinema, 7.2 Canales, Certificado THX, IMAX Enhanced, Dolby Atmos/DTS:X, 8K, HDMI 2.1, Wi-Fi, Bluetooth, Negro, Compatible con Alexa/Google Assistant/Apple Airplay                                                   | 0.572895    |
| OVALTECH            | Ovaltech Brazo de Pared para Monitor 17" - 27", máx. 7kg, Negro                                                                                                                                                                                            | 2.35229     |
| PANASONIC           | Panasonic Teléfono Básico con 13 Memorias, Alámbrico, Blanco                                                                                                                                                                                               | 12.1285     |
| PANASONIC           | Panasonic Teléfono IP con Pantalla LCD 4.3" KX-NT680X, Altavoz, Blanco                                                                                                                                                                                     | 11.9242     |
| PANASONIC           | Panasonic Base para KX-TPA65B, Negro                                                                                                                                                                                                                       | -1.25553    |
| PANDUIT             | Panduit Placa de Pared Ciega Universal, Blanco                                                                                                                                                                                                             | 11.7189     |
| PANDUIT             | Panduit Cable de Fibra Óptica OM4 de 12 Hilos para Interiores/Exteriores, 50/125, Multimodo, Negro - Precio por Metro                                                                                                                                      | 11.3934     |
| PANDUIT             | Panduit Cinta Adhesiva para Aislar, 1 Rollo de 19mm x 20m, Verde                                                                                                                                                                                           | 2.02658     |
| PANDUIT             | Panduit Empalme de Desbordamiento 2x2, Amarillo                                                                                                                                                                                                            | 0.613225    |
| PANDUIT             | Panduit Conexión en T Horizontal para Canaleta, 150 x 100mm, Amarillo                                                                                                                                                                                      | 0.122513    |
| PCTEL               | PCTEL Antena para Radio BOA24006-NF, 2400 - 5MHz, 6dBi                                                                                                                                                                                                     | -0.390204   |
| PEAK TOUR           | Peak Tour Maleta de Viaje Rígida Albania, 22", Candado, Plata                                                                                                                                                                                              | 11.8124     |
| PEAK TOUR           | Peak Tour Maletín de Poliéster Windsor para Laptop 15.6", Negro                                                                                                                                                                                            | 10.902      |
| PELIKAN             | Pelikan Goma de Migajón Tipo Bloque, Blanco, 20 piezas                                                                                                                                                                                                     | -1.39525    |
| PERFECT CHOICE      | Perfect Choice Mochila Essentials para Laptop 15''-17'', Negro                                                                                                                                                                                             | 12.1832     |
| PERFECT CHOICE      | Perfect Choice Dispensador para Gel Antibacterial y Jabón, 0.7L, Automático, Blanco                                                                                                                                                                        | 0.0428439   |
| PILOT               | Pilot Desengrapador de Acero No.6, Negro                                                                                                                                                                                                                   | -1.15221    |
| PNY                 | Tarjeta de Video PNY NVIDIA GeForce RTX 4090 24GB OC XLR8 Gaming Verto EPIC-X RGB TF, 24GB 384-bit GDDR6X, PCI Express x16 4.0                                                                                                                             | 12.9934     |
| POLITEC             | Politec Pintura Acrílica Metálica para Arte Línea 700, 250ml, Bronce, No. 702                                                                                                                                                                              | 1.95159     |
| POLITEC             | Politec Pincel Plano, Pelo Sintético, Mango Corto,  #12, 1 Pieza, para Multitécnica y Decorativa                                                                                                                                                           | 1.94114     |
| POLY                | Poly Teléfono de Diadema CT14, Inalámbrico, DECT 6.0, Negro                                                                                                                                                                                                | 12.1748     |
| POLY                | Poly Cable Extensión para Micrófono, 1.8 Metros, Blanco                                                                                                                                                                                                    | 1.161       |
| POLY                | Poly Kit de Adaptador de Corriente 2200-42740-001, Entrada 100-240V, Salida 48V, Negro                                                                                                                                                                     | 0.852259    |
| POLY                | Poly Base para W440, Negro                                                                                                                                                                                                                                 | -0.81321    |
| POSLINE             | POSline Papel Térmico 45mm x 57mm, 50 Rollos                                                                                                                                                                                                               | 12.4328     |
| POSLINE             | POSline ITT4120 Impresora de Etiquetas, Térmica Directa, USB, 203 x 203 DPI, Negra                                                                                                                                                                         | 2.67133     |
| POWER SONIC         | Power Sonic Batería de Respaldo UL PS-12260-F2, 12V, 26Ah, para Alarmas de Incendio                                                                                                                                                                        | 10.8149     |
| PRECISION           | Precision Kit de Herramientas para Reparaciones en General                                                                                                                                                                                                 | 2.25978     |
| PRECISION           | Precision Candado de Latón PSTA01003, 40mm, 3 Llaves                                                                                                                                                                                                       | 0.397042    |
| PRETUL              | Pretul Rotomartillo ROTO-1/2P6, 1/2", Alámbrico, 550W, Amarillo                                                                                                                                                                                            | 0.530291    |
| PROLICOM            | Prolicom Paños Humedos TOWEL-70, para Pantallas LCD/TFT/Plasma, 2 Piezas                                                                                                                                                                                   | 10.3882     |
| PROVISION ISR       | Provision-ISR Caja de Conexiones para Cámaras FEI-xxxIPx, Blanco                                                                                                                                                                                           | 11.0755     |
| PROVISION ISR       | Provision-ISR Servidor de Video OC-MSCL-S\(DT\)-V2, 256 Canales, 1x HDMI, 4K, 1x RJ-45                                                                                                                                                                     | 0.845797    |
| QIAN                | Teclado POS Qian QPA1702, Alámbrico, PS/2, Negro \(Español\)                                                                                                                                                                                               | 1.4833      |
| QIAN                | Laptop Qian QCL-14N33-W 14" Full HD, Intel Celeron N3350 1.10GHz, 4GB, 120GB SSD, Windows 10 Home 64-bit, Español, Negro                                                                                                                                   | -0.460208   |
| QIAN                | Laptop Qian QCL-14N33 14.1'' Full HD, Intel Celeron N3350 1.10GHz, 4GB, 120GB SSD, Endless, Español, Negro                                                                                                                                                 | -89.97      |
| RADOX               | Radox LED Naranja 245-830, 5mm, 100 Piezas                                                                                                                                                                                                                 | 11.7634     |
| RADOX               | Radox Soporte para Micrófono 490-639, Negro                                                                                                                                                                                                                | 11.5841     |
| RADOX               | Radox Terminal Faston, Hembra, 100 Piezas                                                                                                                                                                                                                  | 11.5543     |
| RADOX               | Radox Trompeta para Perifoneo, 12", Exterior, Gris - no incluye Unidad/Driver                                                                                                                                                                              | 11.0548     |
| RAIDMAX             | Raidmax Kit de Disipador RGB para RAM MX-902F, 5V, Negro                                                                                                                                                                                                   | -0.963639   |
| RASPBERRY           | Raspberry Cable Micro HDMI D Macho - HDMI A Macho, 1 Metro, Blanco                                                                                                                                                                                         | 11.3302     |
| RASPBERRY           | Raspberry Cargador de Pared, 5.1V, 1x USB C , Blanco                                                                                                                                                                                                       | 10.8489     |
| RASPBERRY           | Raspberry Lente para Cámara Thelephoto, 16mm, 10MP, para Raspberry Pi HQ                                                                                                                                                                                   | 10.1941     |
| RCI                 | RCI Estación Manual de Emergencia 904PB, Alámbrico, Azul                                                                                                                                                                                                   | 1.55297     |
| REMINGTON           | Remington Secadora D24A Supercare Pro, 2 Velocidades, 1900W, Negro                                                                                                                                                                                         | 12.045      |
| REMINGTON           | Remigton Cortadora de Cabello HC5850, 15 Piezas, Amarillo/Negro                                                                                                                                                                                            | 1.4486      |
| RESIDEO             | Resideo Control Remoto de 4 Botones, Inalámbrico, Negro, Compatible con Panel ProSeries                                                                                                                                                                    | 0.522474    |
| RF INDUSTRIES       | RF Industries Conector TNC Macho de Anillo Plegable para Cable RG-11/U                                                                                                                                                                                     | 2.30244     |
| RHEEM               | Rheem Calentador de Agua 89V40, Eléctrico 220V, 152 Litros/Hora, Gris                                                                                                                                                                                      | 1.49699     |
| RHINO               | Rhino Báscula Electrónica BAR-8RS, hasta 40Kg, Negro/Gris                                                                                                                                                                                                  | 9.87944     |
| ROMMS               | Romms Pila Telefónica Recargable, 3.6V, 600mAh                                                                                                                                                                                                             | 0.0662771   |
| ROYAL               | Royal Lampara Dectectora de Billetes Falsos ELEROYDETBUV1, Luz Ultravioleta, Detector magnético, Negro                                                                                                                                                     | 13.6848     |
| ROYAL               | Royal Despachador de Agua RAQ500, 18.9 Litros, Blanco                                                                                                                                                                                                      | 11.7453     |
| ROYAL TALENS        | Royal Talens Tinta Acuarela con Gotero Ecoline, 30ml, Sepia Oscuro No. 440                                                                                                                                                                                 | 0.194056    |
| SAKURA              | Sakura Marcador Pen Touch 42100, Punto Extra Fino, Blanco                                                                                                                                                                                                  | 0.101913    |
| SAKURA              | Sakura Estilógrafo Pigma Micron 03, 0.35mm, Negro                                                                                                                                                                                                          | -99.6282    |
| SAMSUNG             | Samsung Flip 2.0 Pantalla Comercial LCD Touch 55", Blanco - no Incluye Base                                                                                                                                                                                | 10.613      |
| SAMSUNG             | Laptop Samsung Chromebook 4+ 15.6" Full HD, Intel Celeron N4000 1.10GHz, 4GB, 32GB eMMc, Chrome OS, Inglés, Plata                                                                                                                                          | -0.379825   |
| SAMSUNG             | Laptop Samsung Chromebook 4 XE310XBA-K01US 11.6" HD, Intel Celeron N4000 1.10GHz, 4GB, 32GB, Chrome OS, Plata                                                                                                                                              | -0.616531   |
| SAMSUNG             | Laptop Samsung Chromebook 4 11.6" HD, Intel Celeron N4000 1.10GHz, 4GB, 32GB eMMC, Chrome OS, Inglés, Plata                                                                                                                                                | -99.9028    |
| SANAIRE             | Sanaire Campana Phillax, 61cm, Gris                                                                                                                                                                                                                        | 10.6146     |
| SANDISK             | SSD Externo SanDisk Portable, 1TB, USB C, Negro                                                                                                                                                                                                            | 13.837      |
| SAXXON              | Saxxon Adaptador de Corriente PSU1205D, Entrada 100 - 240V, Salida 12V                                                                                                                                                                                     | 11.1824     |
| SEAGATE             | Disco Duro para NAS Seagate IronWolf Pro 3.5" de 1 a 24 Bahías, 10TB, SATA III, 6Gbit/s, 7200RPM, 256MB Caché                                                                                                                                              | 11.01       |
| SEAGATE             | Disco Duro Interno Seagate Barracuda Pro 2.5'', 1TB, SATA III, 6 Gbit/s, 7200RPM, 128MB Caché                                                                                                                                                              | 1.55292     |
| SECO-LARM           | Seco-Larm Botón de Salida SD-7201-GCPE1, Alámbrico, Acero Inoxidable                                                                                                                                                                                       | 2.04434     |
| SECO-LARM           | Seco-Larm Módulo Relevador SR-2112-C7AQ/10, 7A, 12-24V                                                                                                                                                                                                     | -0.939802   |
| SFIRE               | SFire Cople Recto para Tubería de Aspiración, Rojo                                                                                                                                                                                                         | -0.953557   |
| SHURE               | Shure Kit Micrófonos para Bombos PGADRUMKIT5, Alámbrico, Negro                                                                                                                                                                                             | 0.339661    |
| SL PROLIGHT         | SL Prolight Reflector LED Flood Perfetti, 150W, Negro                                                                                                                                                                                                      | 11.5158     |
| SOLAX               | SolaX Inversor para Interconexión Grid-Tie X1-1.1-S-D, 1100W, 450V                                                                                                                                                                                         | 1.11341     |
| SONY                | Sony Gamepad DualSense para PlayStation 5, Inalámbrico, Bluetooth, Azul                                                                                                                                                                                    | 12.9275     |
| SONY                | Sony Grabadora Reportera UX570, 4GB, USB, Negro                                                                                                                                                                                                            | 10.023      |
| SONY                | Sony PlayStation 4 Slim 500GB, WiFi, Bluetooth 4.0, Negro                                                                                                                                                                                                  | 1.80284     |
| SONY                | Sony PlayStation 5 Digital Edition 825GB, WiFi, Bluetooth 5.1, Blanco/Negro ― Incluye Juego Horizon Forbidden West                                                                                                                                         | 1.03445     |
| SONY                | Horizon II Forbidden West, PlayStation 5                                                                                                                                                                                                                   | 0.0140284   |
| SPARKFUN            | Sparkfun Kit de Jumpers Hembra - Hembra, 20 Piezas, Multicolor                                                                                                                                                                                             | -0.246688   |
| StarTech.com        | StarTech.com Cable KVM Ultra Delgado 2 en 1, USB/VGA Macho - VGA Macho, 3 Metros, Negro ― Envío gratis limitado a 10 unidades por cliente                                                                                                                  | 12.0324     |
| StarTech.com        | Startech.com Cable Adaptador USB 3.0 con UASP - SATA III para Disco Duro 2.5''                                                                                                                                                                             | 9.80627     |
| StarTech.com        | StarTech.com Cable RJ45 Macho - Serial DB9 Hembra, 1.8 Metros, Azul                                                                                                                                                                                        | 9.78431     |
| StarTech.com        | StarTech.com Tapete Antiestatico de PVC, 60x70cm, Beige                                                                                                                                                                                                    | 1.16383     |
| StarTech.com        | StarTech.com Adaptador Convertidor de SSD mSATA - SATA de 2.5''                                                                                                                                                                                            | 1.16324     |
| STEEL PRO           | Steel Pro Autoestéreo XZR-070, FM/MP3, Bluetooth/USB, Negro                                                                                                                                                                                                | 10.5914     |
| STEREN              | Steren Candado de Combinación para Laptops COM-228, 1.7 Metros, Marrón                                                                                                                                                                                     | 11.3941     |
| STEREN              | Steren Pantalla de Proyección PRO-005, 100", Blanco                                                                                                                                                                                                        | 1.42881     |
| STEREN              | Steren Purificador de Aire AIR-350, 16m², Gris/Blanco                                                                                                                                                                                                      | 0.851781    |
| STEREN              | Steren Batería para Radio RAD-411, 3.7V, 1700mAh, Compatible con RAD-410                                                                                                                                                                                   | 0.843031    |
| STEREN              | Steren Filtro para Purificador de Aire HEPA H13, 1 Pieza, para Ionizador AIR-350                                                                                                                                                                           | 0.842481    |
| STI                 | STI Botón de Salida de Emergencia, Alámbrico, Amarillo, Texto en Inglés                                                                                                                                                                                    | 11.5566     |
| STYLOS              | Stylos Tripié para Bocina STASOX1B, hasta 102cm, Negro                                                                                                                                                                                                     | 11.6034     |
| SURTEK              | Surtek Juego de Herramientas JPS01, 3 Piezas, Negro                                                                                                                                                                                                        | 10.5035     |
| SURTEK              | Surtek Motobomba a Gasolina MG533A, 60.000L/h, 6.7HP, Negro                                                                                                                                                                                                | 1.41967     |
| SURTEK              | Surtek Polipasto POLPAL2, 1500Kg, Cadena 1.5 Metros, Amarillo                                                                                                                                                                                              | 0.898774    |
| SURTEK              | Flexómetro Surtek B122081, 5 Metros, 2.5cm, Negro/Amarillo                                                                                                                                                                                                 | 0.852779    |
| SURTEK              | Porta Manguera de Pared Surtek 130362, hasta 75 Metros, Gris                                                                                                                                                                                               | 0.437644    |
| SYSCOM              | Syscom Brazo para Torre Arriostrada Tipo Bastón, para STZ30G/STZ35G/STZ45G                                                                                                                                                                                 | -0.725376   |
| TACX                | Tacx Kit Rodillos Entrenadores de Ciclismo Inteligentes Boost, ANT+, Bluetooth, Azul/Negro - Incluye Soporte y Cierre Rápido                                                                                                                               | 0.0749144   |
| TARGUS              | Targus Funda Universal SafeFit para Tablet 8.5", Giro 360°, Negro                                                                                                                                                                                          | 2.67133     |
| TARGUS              | Targus Filtro de Privacidad 4Vu para Monitor 18.5''                                                                                                                                                                                                        | 0.734807    |
| TAURUS              | Taurus Ventilador Bolt, 2 Velocidades, 16", Blanco                                                                                                                                                                                                         | 13.3601     |
| TAURUS              | Taurus Cafetera Coffemax 6, 6 Tazas, Negro/Transparente                                                                                                                                                                                                    | 13.0992     |
| TAURUS              | Taurus Licuadora Nature, 1 Litros, 400W, 4 Velocidades, Negro                                                                                                                                                                                              | 11.7349     |
| TAURUS              | Taurus Recortadora MINOS, Negro/Gris - incluye Cortadora Mythos                                                                                                                                                                                            | 11.6919     |
| TAURUS              | Taurus Exprimidor de Cítricos CR100, 0.5 Litros, Azul Navy                                                                                                                                                                                                 | 11.3745     |
| TECHZONE            | TechZone Maletín de Nílon TZ16BCP33 para Video Proyectores, Negro                                                                                                                                                                                          | -1.31451    |
| TECNOLITE           | Tecnolite Lámpara LED Inteligente SPIRIT, WiFi, RGB, 12.5W, 810 Lúmenes, Blanco                                                                                                                                                                            | 2.75591     |
| TECNOLITE           | Tecnolite Humidificador y Difusor de Aromas Scent, 300/500ml, Café                                                                                                                                                                                         | 0.796845    |
| TECNOLITE           | Tecnolite Lámpara LED para Techo Empotrable Regulus, Interiores, Luz de Día, 7W, 500 Lúmenes, Blanco, para Casa                                                                                                                                            | 0.723832    |
| THOMSON             | Laptop Thomson WWN15i5-4BK256 15.6" Full HD, Intel Core i5-5257U 2.70GHz, 4GB, 256GB SSD, Windows 10 Home 64-bit, Inglés, Negro                                                                                                                            | 11.8566     |
| THOMSON             | Laptop Thomson NEOX14 14" Full HD, Intel Celeron N3350 1.10GHz, 4GB, 64GB eMMC, Windows 10 Home 64-bit, Inglés, Rosa                                                                                                                                       | -98.9656    |
| THOMSON             | Laptop Thomson NEOX14 14" Full HD, Intel Celeron N3350 1.10GHz, 4GB, 64GB eMMC, Windows 10 Home 64-bit, Inglés, Azul                                                                                                                                       | -98.9901    |
| THOMSON             | Laptop Thomson NEO14A 14" Full HD, Intel Atom X5-Z8350 1.44GHz, 4GB, 64GB eMMC, Windows 10 Home 64-bit, Inglés, Blanco                                                                                                                                     | -98.998     |
| TIMCO               | Timco Hervidor de Agua Eléctrica JEV02, 1.7 Litros, 1200W, Negro                                                                                                                                                                                           | 11.9376     |
| TOTAL GROUND        | Total Ground Kit de Tierra Física TG45AB, 45A - incluye Electrodo/H2Ohm/Registro                                                                                                                                                                           | 1.60291     |
| TOUGHBOOK PANASONIC | Laptop Panasonic Toughbook FZ-55D2601KM 14" HD, Intel Core i5-1145G7 2.60GHz, 16GB, 512GB SSD, Windows 10 Pro 64-bit, Inglés, Negro                                                                                                                        | 2.17092     |
| TOUGHBOOK PANASONIC | Laptop Panasonic Toughbook  FZ-55D2601VM 14" HD, Intel Core i5-1145G7 2.60GHz, 16GB, 512GB SSD, Windows 10 Pro 64-bit, Inglés, Negro                                                                                                                       | 1.80244     |
| TOUGHBOOK PANASONIC | Laptop Panasonic Toughbook FZ-55DZ03MTM 14" HD, Intel Core i5-1145G7 2.60GHz, 16GB, 512GB SSD, Windows 10 Pro 64-bit, Español, Negro                                                                                                                       | -0.726996   |
| TP-LINK             | TP-Link Adaptador Bluetooth TL-WN725N, USB, Negro, 10 Piezas — Configuración Especial, 1 Año de Garantía                                                                                                                                                   | 13.3912     |
| TP-LINK             | TP-Link Extensor de Rango TL-WA855RE, Inalámbrico, 300 Mbit/s, 5 Piezas — Configuración Especial, 1 Año de Garantía                                                                                                                                        | 13.3494     |
| TP-LINK             | Switch TP-Link Fast Ethernet TL-SF1008D, 10/100Mbps, 1.6Gbit/s, 8 Puertos, 1000 Entradas – No Administrable                                                                                                                                                | 12.9171     |
| TP-LINK             | TP-Link TG-3468 Tarjeta de Red PCI Express, Alámbrico, IEEE 802.3/3u/3ab, 802.3x, 802.1q/1p                                                                                                                                                                | 12.8824     |
| TP-LINK             | Router TP-Link Fast Ethernet de Banda Dual Firewall ARCHER C24, Inalámbrico, 433Mbit/s, 5x RJ-45, 2.4/5GHz, 4 Antenas Externas                                                                                                                             | 12.4995     |
| TRAMONTINA          | Tramontina Juego de Cuchillos Cronos, 3 Piezas, Acero Inoxidable                                                                                                                                                                                           | 13.2065     |
| TRAMONTINA          | Tramontina Juego de Cubiertos Leme, 25 Piezas, Acero Inoxidable                                                                                                                                                                                            | 11.4143     |
| TRIPP LITE          | No Break Tripp Lite OMNISMART700M, 450W, 700VA                                                                                                                                                                                                             | 14.4327     |
| TRIPP LITE          | Tripp Lite Cable de Carga Certificado MFi Lightning Macho - USB C Macho, 1 Metro, Blanco                                                                                                                                                                   | 14.0951     |
| TRIPP LITE          | Tripp Lite Cable TMS Digital DVI-D Macho - DVI-D Macho, 3.05 Metros, Negro                                                                                                                                                                                 | 12.6415     |
| TRIPP LITE          | Tripp Lite Adaptador DisplayPort Macho - HDMI/DVI/VGA Hembra, Negro                                                                                                                                                                                        | 10.5244     |
| TRIPP LITE          | Tripp Lite Cable Patch Cat5e UTP Moldeado Sin Enganches RJ-45 Macho - RJ-45 Macho, 30.48 Metros, Azul                                                                                                                                                      | 10.2194     |
| TRUPER              | Truper Sopladora SOPLA-960, 960W, Naranja/Negro                                                                                                                                                                                                            | 1.79516     |
| TRUPER              | Escalera de Tijera Truper EST-23, Aluminio, 2.4 Metros, 3 Peldaños, hasta 175Kg                                                                                                                                                                            | 1.2448      |
| TRUPER              | Cavador Truper CA-38, Puño T, 122cm, con Mango de Acero                                                                                                                                                                                                    | 0.572755    |
| TRUPER              | Truper Compresor de Aire Vertical Libre de Aceite COMP-50S, 50L, 2/3HP, 127V                                                                                                                                                                               | -0.0925474  |
| TRUPER              | Truper Manguera de Hule MAN-AP-15-3/8, 300PSI, 3/8",  15 Metros, Negro                                                                                                                                                                                     | -0.295698   |
| TWELVE SOUTH        | Twelve South Funda SuitCase para MacBook Pro/Air 16", Gris                                                                                                                                                                                                 | -0.362566   |
| TXPRO               | TXPRO Cable Programador para Radio, USB, Negro, para ICOM IC-F4161/ 3161                                                                                                                                                                                   | 0.106492    |
| TXPRO               | TXPRO Funda de Plástico TXCDEP450, Negro, para Motorola DEP450                                                                                                                                                                                             | -0.00608308 |
| UBIQUITI NETWORKS   | Ubiquiti Networks Antena Radio airFiber 60 LR, 60GHz, hasta 12Km                                                                                                                                                                                           | 13.9233     |
| UBIQUITI NETWORKS   | Ubiquiti Networks NVR de 4 Canales UNVR para 4 Discos Duros, max. 4GB, 1x RJ-45                                                                                                                                                                            | 10.9832     |
| UBIQUITI NETWORKS   | Ubiquiti Networks Controlador Inalámbrico UniFi Cloud Key Gen2 Plus, Gigabit Ethernet, 1x RJ-45                                                                                                                                                            | 10.0609     |
| UBIQUITI NETWORKS   | Ubiquiti Networks Terminal de Línea Óptica UFiber OLT4, 4x PON, 1x SFP                                                                                                                                                                                     | 9.55267     |
| UBIQUITI NETWORKS   | Ubiquiti Networks Adaptador e Inyector de PoE POE-24-7W-G, 1000 Mbit/s, Gigabit Ethernet, 24V, 2x RJ-45                                                                                                                                                    | 2.77158     |
| UGREEN              | Ugreen Hub USB C 3.2 - 4x USB A 3.0, 1x HDMI, Gris                                                                                                                                                                                                         | 3.16087     |
| UGREEN              | Ugreen Funda Impermeable para Smartphone, Negro/Transparente                                                                                                                                                                                               | 0.362025    |
| URREA               | Urrea Multicontacto, 2 Entradas/2 Puertos USB, 15A, 127V, Blanco                                                                                                                                                                                           | 10.7997     |
| URREA               | Urrea Esmeril de Banco EB906, 570W, 6", Rojo/Negro                                                                                                                                                                                                         | 2.7559      |
| URREA               | Urrea Destornillador de Torque 6105B, 1/4", Negro                                                                                                                                                                                                          | 2.75589     |
| URREA               | Engrapadora Urrea Neumática EN916, Calibre 22, 185 Grapas, Negro/Gris                                                                                                                                                                                      | 2.75589     |
| URREA               | Urrea Extensión de Dado 546430, 1/2", 75.5cm, Plata                                                                                                                                                                                                        | 2.75589     |
| VERBATIM            | Teclado Verbatim 70708, Inalámbrico, USB, Negro \(Español\)                                                                                                                                                                                                | 13.6321     |
| VERBATIM            | Verbatim Cargador Dual para Nintendo Switch, Negro                                                                                                                                                                                                         | 10.256      |
| VERBATIM            | Verbatim Torre de Discos Virgenes para DVD, DVD+R, 8x, 50 Discos \(97000\)                                                                                                                                                                                 | 1.20632     |
| VERBATIM            | Verbatim Torre de Discos Virgenes Imprimibles para CD, CD-R, 52x, 100 Discos                                                                                                                                                                               | 1.16593     |
| VICA                | Vica Multicontacto SUPVIC050, 3 Salidas, 4x USB, Blanco                                                                                                                                                                                                    | 2.30279     |
| VICTORINOX          | Victorinox Navaja de Bolsillo Swiss Champ, 33 Usos, Rojo                                                                                                                                                                                                   | 10.7055     |
| VORAGO              | Vorago Soporte de Pared TM-300 para Pantalla 13" - 42", hasta 25kg, Negro                                                                                                                                                                                  | 13.4294     |
| VORAGO              | Laptop Vorago Alpha Plus 14" HD, Intel Celeron N4020 1.10GHz, 8GB, 500GB HDD + 64GB eMMC, Windows 10 Pro 64-bit, Español, Plata                                                                                                                            | 10.8427     |
| VORAGO              | Laptop Vorago Alpha Plus 14" HD, Intel Celeron N4020 1.10GHz, 4GB, 500GB HDD + 64GB eMMC, Windows 10 Pro 64-bit, Español, Plata                                                                                                                            | -0.183435   |
| VORAGO              | Laptop Vorago Alpha Plus 14" HD, Intel Celeron N3350 1.10GHz, 4GB, 500GB + 64GB eMMC, Windows 10 Home 64-bit, Español, Plata                                                                                                                               | -0.533542   |
| VORAGO              | Laptop Vorago Alpha Plus 14" HD, Intel Celeron N4020 1.10GHz, 4GB, 500GB HDD + 64GB eMMC, Windows 10 Pro 64-bit, Español, Plata ― incluye Impresora Xerox 3020 Láser WiFi                                                                                  | -0.726926   |
| VSG                 | Teclado Gamer VSG Mintaka RGB 60%, Teclado Mecánico, Switch Kailh Blue, Alámbrico, Blanco \(Español\)                                                                                                                                                      | 9.9104      |
| VSSL                | VSSL Extensor de Audio A.6X, 6 Zonas, 12 x 50W, Wi-Fi, Bluetooth, con Chromecast y Google Assistant                                                                                                                                                        | -0.237025   |
| WAVESHARE           | Waveshare Pantalla 5" para Placas de Desarrollo Raspberry Pi WS-18396, 800 x 480 Pixeles, Negro                                                                                                                                                            | 10.457      |
| WEBOOST             | Weboost Kit de Amplificador de Señal Celular, 3G/4G, 700MHz, 70dB, 3000² Metros                                                                                                                                                                            | 1.23381     |
| WEBOOST             | WeBoost Antena Multibanda para Celular 314440, 698-960, 1710-2700MHz, 7.62dBi                                                                                                                                                                              | 0.686181    |
| WESTERN DIGITAL     | SSD Western Digital WD Green, 1TB, SATA III, 2.5", 7mm                                                                                                                                                                                                     | 14.9972     |
| WESTERN DIGITAL     | Disco Duro para Videovigilancia Western Digital Purple Surveillance 3.5", 6TB, SATA, 6 Gbit/s, 256MB Cache                                                                                                                                                 | 13.5503     |
| WESTERN DIGITAL     | Disco Duro Interno Western Digital WD Blue 3.5", 5TB, SATA lll, 6 Gbit/s, 5400RPM, 64MB                                                                                                                                                                    | 13.0678     |
| WESTINGHOUSE        | Westinghouse Horno Eléctrico de Convección y Rosticero WKTOGE43BK, 1600W, 43 Litros, Negro                                                                                                                                                                 | 13.122      |
| WESTINGHOUSE        | Westinghouse Parrilla Grill Eléctrica Panini, Antiadherente, 1400W, Negro                                                                                                                                                                                  | 12.2545     |
| WHIRLPOOL           | Whirlpool Refrigerador WT1870A, 18 Pies Cúbicos, Plata                                                                                                                                                                                                     | 10.8636     |
| WHIRLPOOL           | Whirlpool Enfriador de Vinos WW2110S, 5 Estantes, 21 Botellas, Gris                                                                                                                                                                                        | 1.17092     |
| WINLAND             | Winland Sensor para Nivel de Agua WB-200, Alámbrico, Blanco                                                                                                                                                                                                | 1.67065     |
| WINLAND             | Winland Sensor Externo de Alta Temperatura EnviroAlert, 0 - 150 °C, para EA200-12                                                                                                                                                                          | 1.51879     |
| X-MEDIA             | X-Media Adaptador USB 3.0 Macho - IDE, Negro                                                                                                                                                                                                               | -1.1273     |
| XEROX               | Xerox Bandeja de 650 Hojas, para C310                                                                                                                                                                                                                      | 1.80245     |
| XEROX               | Fusor Xerox 115R00139, 200.000 Páginas, para VersaLink B600/B605/ B610/B615                                                                                                                                                                                | 1.6854      |
| XEROX               | Xerox Cartucho de Desperdicio 108R00982                                                                                                                                                                                                                    | 1.16328     |
| XEROX               | Xerox Kit de Unidad de Transferencia 108R01122, 100.000 Páginas                                                                                                                                                                                            | 0.704281    |
| XEROX               | Xerox Módulo Realizador de Folletos 497K20590, para AltaLink C81XX/B81XX ― Requiere EZK para su Correcto Funcionamiento, se Vende por Separado                                                                                                             | 0.0881912   |
| XIAOMI              | Xiaomi Báscula Corporal Inteligente Mi Body Composition Scale 2, Android/iOS, hasta 150Kg, Blanco, Medición de IMC/Grasa Corporal/Masa Ósea/Agua/Masa Muscular/Proteína/Peso/Peso Ideal                                                                    | 11.2494     |
| XIAOMI              | Xiaomi Papel Fotográfico, 287g/m², 2" x 3", 20 Hojas                                                                                                                                                                                                       | 11.0117     |
| XIAOMI              | Xiaomi Selfie Stick, Bluetooth, Gris                                                                                                                                                                                                                       | -0.475966   |
| XP-PEN              | Tableta Gráfica XP-PEN Deco Fun L, 25.4 x 159.2cm, Alámbrico, USB-C, Rojo Carmín                                                                                                                                                                           | 10.4297     |
| XPG                 | XPG Tiras LED con Control Prime ARGB, 60cm x 10mm, Negro                                                                                                                                                                                                   | 10.582      |
| XPG                 | Laptop Gamer XPG Xenia 14 14" Full HD, Intel Core i7-1165G7 2.80GHz, 16GB, 512GB SSD, Windows 10 Home 64-bit, Inglés, Negro                                                                                                                                | -0.0704173  |
| XPG                 | Laptop Gamer XPG Xenia 15 KC 15.6" Quad HD, Intel Core i7-11800H 2.30GHz, 32GB, 1TB SSD, NVIDIA GeForce RTX 3070, Windows 10 Home 64-bit, Inglés, Negro                                                                                                    | -0.151255   |
| XPG                 | Laptop XPG Gamer Xenia 14 14" Full HD, Intel Core i5-1135G7 2.40GHz, 16GB, 512GB SSD, Windows 10 Home 64-bit, Español, Negro                                                                                                                               | -0.270965   |
| XPG                 | Laptop Gamer XPG Xenia 14 14" Full HD, Intel Core i7-1165G7 2.80GHz, 16GB, 512GB SSD, Windows 10 Home 64-bit, Español, Negro                                                                                                                               | -0.27173    |
| XSS                 | XSS Micrófono CM-158B, Alámbrico, XLR, Negro                                                                                                                                                                                                               | 13.5794     |
| XZEAL               | Xzeal Silla Gamer XZ25, hasta 150Kg, Negro/Azul                                                                                                                                                                                                            | 13.01       |
| XZEAL               | XZEAL Webcam XZ200, 1920 x 1080 Pixeles, Negro                                                                                                                                                                                                             | 11.993      |
| YAELTEX             | Yaeltex Módulo Kilomux tipo Fader F41, para Placas de Desarrollo, 1 Pieza                                                                                                                                                                                  | 10.5923     |
| YEALINK             | Yealink Adaptador de Corriente PS 12V1A, para Teléfonos IP T18P/T2/T41P/T42G                                                                                                                                                                               | 0.25899     |
| YEASTAR             | Yeastar Tarjeta de Expansión YS-MDO2, 2 Canales FXO, para S412/S20/S50/S100/S300                                                                                                                                                                           | 0.136984    |
| YLI ELECTRONIC      | YLI Electronic Cerradura Electromagnética YM-500NW, 6 x 18.5cm, 500Kg                                                                                                                                                                                      | 10.5846     |
| ZAGG                | Zagg Protector de Pantalla para iPad Pro 11 11" Glass+ Visionguard, Transparente                                                                                                                                                                           | 0.302471    |
| ZEBRA               | Zebra Impresora Móvil ZQ630, Térmica Directa, Inalámbrico, 203 x 203DPI, Ethernet, Bluetooth, USB, Serial, Negro                                                                                                                                           | 12.9353     |
| ZEBRA               | Zebra Rollo de Etiqueta Z-Perform 2000T 4'' x 2'', 1320 Etiquetas, 1 Pieza                                                                                                                                                                                 | 10.9432     |
| ZEBRA               | Zebra Card Studio 2.0, 1 Licencia Estándar, Windows                                                                                                                                                                                                        | 2.75589     |
| ZEBRA               | Zebra Kit de Montaje para XC6, Negro                                                                                                                                                                                                                       | 2.67131     |
| ZEBRA               | Zebra Correa de Hombro para TC8000, Negro                                                                                                                                                                                                                  | 2.67093     |
| ZKTECO              | ZKTeco Control de Acceso y Asistencia Biométrico SpeedFace V5LP, 6.000 Rostros, 10.000 Huellas, RS-485                                                                                                                                                     | 11.5237     |
| ZKTECO              | ZKTeco Panel de Control inBio-460BOX para 4 Puertas, incluye Gabinete + Fuente                                                                                                                                                                             | 10.8383     |
| ZKTECO              | ZKTeco Unidad de Respaldo de Energía para Lectores Biométricos, 12V                                                                                                                                                                                        | 1.06838     |
| ZKTECO              | ZKTeco Monitor para Videoportero VDPI-B3, 7", Altavoz, Alámbrico, Blanco                                                                                                                                                                                   | 0.979202    |



