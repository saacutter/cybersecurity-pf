# Introduction
For this activity, I researched some of the different (and common) access control devices used today. The devices I chose are a mix of categories of devices (i.e. the first four) and one specific type of device (i.e. the last one) because this allowed for further exploration of the different devices available and gave the most varied implementations of access control. To find these devices, I used the following lists as a starting point to explore further:
- https://www.getscw.com/knowledge-base/types-of-access-control-systems
- https://www.macsecuritysystems.co.uk/news/3-types-of-access-control-systems
- https://www.fortinet.com/resources/cyberglossary/access-control

## PIN/Keypad Access Control
Access control keypads are similar to traditional key-based locks, but replace the physical access credential (i.e. a possession factor) which can be easily lost with a PIN code (i.e. a knowledge factor). They are typically a simple keypad connected to a deadbolt which is controlled by an electric motor. If the individual is authenticated by entering the correct code, the door will unlock allowing them to access the area.

These keypads can be cost-effective since they don't need physical credentials to operate, and the codes can be changed quickly if a security incident were to occur. However, changing the codes needs to be done regularly to avoid security incidents which can be time-consuming if there are multiple keypads. They also may lack an audit trail to follow if a security incident were to occur, making it difficult to detect the intrusion.

An example of a keypad access control device is the HID-40KNKS-02.

## Card/Fob Access Control
These access control systems use electronic credentials (which are stored on an electronic device like keycards or fobs) to enforce access control. These credentials are programmable and trackable, making them an effective choice for an access control system which needs to manage several people as it allows all actions to be tracked in the event of a security incident. These access control systems consist of the credentials (i.e. the keycard/fob/etc) and a reader, which scans the credentials on the device (often using RFID technology but other systems also exist) to determine whether the individual is authorised to enter the controlled area and unlocks the door electronically if they are. These access control systems are mostly used in buildings where there are lots of rooms which need different authorisations, like residential complexes (i.e. hotels, student accommodation, etc) and corporate offices.

There are some advantages to using these systems. Because the credentials are electronic, if the device is ever lost or misplaced then permissions associated with that credential can be revoked instantly which cannot be done with a physical key. It also allows access to be logged at all times, leaving an evidence trail that can be followed in the event of a security incident. Electronic credentials also allow for granular control with flexible/specific permissions for individual people (which can also be done temporarily if necessary) while still being able to use the same terminals at every access point. However, there are still some weaknesses with these systems. If the credential is stolen without the owner's knowledge (or the owner doesn't report it stolen), then an unauthorised individual can gain access to the building mostly undetected. It also relies on the individual keeping their credential on their person at all times, as forgetting it means that they can't access areas they need to.

An example of a card access control device is the HID Signo 20 Reader.

## Biometric Access Control
Biometric access control systems use physical characteristics (i.e. inherence factors) which are unique human features to enforce access control. These systems work by capturing the physical characteristic being used of each individual who needs access, which creates a sort of digital template of the biometric which is then stored in some sort of database (which varies based on local privacy regulations). These characteristics are then scanned at biometric scanners or readers, which authorises the individual if the new scan matches the previous scan and unlocks the door with an electronic signal. Because these features are unique to individuals, they are preferred for high-risk areas. There are several types of biometric access control systems, including fingerprint, facial recognition, eye scans, retinal scans, iris scans, voice recognition, or vein matching.

Unlike knowledge factors and possession factors which can be lost, stolen, or shared, inherence factors cannot significantly change and are unique to individuals reducing the risk of unauthorised access. These characteristics are also difficult (or impossible) to copy, meaning that they are more secure than other access control systems. They are also convenient systems for users because they don't have to carry anything extra with them or remember anything as they will always have these characteristics on them. However, lower quality biometric scanners may be vulnerable to attacks like lower accuracy if the characteristic is obscured or spoofing the sensor using an image of the characteristic allowing for unauthorised access.

An example of a biometric access control device is the HID Amico Biometric Facial Recognition Reader.

## Mobile Access Control
Mobile access control uses mobile devices (e.g. smartphones, tablets, wearable devices, etc) to enforce access control. It uses mobile credentials, which are unique digital keys issued to individuals which have the permissions they need. These credentials are shared to the individual's phone using a method like an app, website link, or QR code depending on how the system is set up. To enhance the security of these credentials, they are often encrypted on the device. Once the device has the credential, it can be used on access readers which use Bluetooth Low Energy or NFC (depending on the reader) to transmit the credential. The reader then validates the credential, and if the individual is authenticated (i.e. they have the necessary permissions) then the area will be unlocked.

Having credentials stored on individuals' mobile devices is convenient (as most people always have their devices on their person) which, consequently, also reduces the chance of losing them. Similar to keycard credentials, mobile credentials can be revoked instantly if it is ever required (for example when an employee leaves an organisation or an individual's phone is lost). They also allow credentials to be managed remotely, allowing for easier management when there are a large amount of users. Some systems may also be able to create alerts when suspicious activity is detected.

An example of a mobile access control device is the HID Mobile Access system.

## Turnstiles
Turnstiles are physical barriers used to control access in areas with large numbers of people and limit access to exclusive areas. They are generally designed with some sort of mechanical or electrical barrier (such as doors or arms) which moves/rotates in a single direction and are fixed to the ground in some way. In general, they only allow one person through at any given time and are integrated with an access control system to only permit authorised individuals entry to the designated area. Access control is typically enforced with some sort of key (usually a keycard but it can be other things like biometrics or keypads) which allows the barrier to unlock (either for an amount of time or until it has rotated one person's width, depending on the barrier) at which point it locks again which reduce tailgating and other forms of unauthorised entry. In some cases where access control isn't required, these turnstile systems are still used to manage congestion effectively (and are often designed differently, like with swinging glass doors). Turnstiles are often combined with other barriers like walls to ensure that people can only enter through the turnstiles to ensure that any people in the area are authorised. They are commonly used in areas like public transport stations (to validate fares and manage the foot traffic effectively), commercial buildings (to ensure that only authorised individuals like employees are permitted), and entertainment venues (to help manage congestion during entry and ensure that only ticket holders can enter).

There are a few different types of turnstiles. These include waist-high turnstiles (which feature waist-level barriers providing a basic level of access control), tripod turnstiles (which have a cylinder of three rotating arms on angle to allow one person to pass through each rotation), full-height turnstiles (which have barriers that cover the floor to the ceiling offering higher security), optical turnstiles (which use light to detect entry), and speed gates (which use retractable glass or acrylic barriers that open automatically when an individual is authenticated).

<br>

# References
M. Nederlanden. "What Types Of Access Control Systems Are There?". Security Camera Warehouse, Inc. Accessed: Mar. 31, 2026. [Online]. Available: https://www.getscw.com/knowledge-base/types-of-access-control-systems

MAC Security Systems Ltd. "3 Types of Access Control Systems: Which One Is Right for Your Premises?". Accessed: Mar. 31, 2026. [Online]. Available: https://www.macsecuritysystems.co.uk/news/3-types-of-access-control-systems

Fortinet, Inc. "What Is Access Control?". Accessed: Mar. 31, 2026. [Online]. Available: https://www.fortinet.com/resources/cyberglossary/access-control

Motorola Solutions, Inc. "Guide to keypad access control systems and door locks". Accessed: Mar. 31, 2026. [Online]. Available: https://www.avigilon.com/blog/keypad-access-control

Defend Security Group Pty Ltd. "HOW SECURE ARE ACCESS KEYPADS FOR BUILDING ENTRY?". Accessed: Mar. 31, 2026. [Online]. Available: https://defendsecuritygroup.com.au/how-secure-are-access-keypads-for-building-entry/

Access Professional Systems. "What Is a Key Card and Key Fob Access Control System?". Accessed: Mar. 31, 2026. [Online]. Available: https://accessprofessionals.com/what-is-a-key-card-and-key-fob-access-control-system/

M. Maxsenti. "Guide to Key Card Entry Systems". Genea Energy Partners, Inc. Accessed: Mar. 31, 2026. [Online]. Available: https://www.getgenea.com/blog/card-access-systems/

Gallagher Group Limited. "From fingerprints to facial recognition: An introduction to Biometric Access Control". Accessed: Mar. 31, 2026. [Online]. Available: https://security.gallagher.com/en/Blog/An-Introduction-to-Biometric-Access-Control

Motorola Solution, Inc. "Guide to biometric door locks and access control security". Accessed: Mar. 31, 2026. [Online]. Available: https://www.avigilon.com/blog/biometric-access-control

Motorola Solutions, Inc. "Understanding mobile credentials and mobile access control". Accessed: Mar. 31, 2026. [Online]. Available: https://www.avigilon.com/blog/mobile-credentials

Assa Abloy AB. "Your Guide to Smartphone Door Access & Commercial Access Control. Say goodbye to keys!". Accessed: Mar. 31, 2026. [Online]. Available: https://www.assaabloy.com/au/en/stories/blog/your-guide-to-smartphone-door-access-commercial-access-control

Kisi Inc. "Mobile access control guide". Accessed: Mar. 31, 2026. [Online]. Available: https://www.getkisi.com/guides/mobile-access-control-guide

Assa Abloy AB. "Seamless Mobile Access: The New Workplace Standard". Accessed: Mar. 31, 2026. [Online]. Available: https://www.hidglobal.com/solutions/mobile-access-solutions

Ezi Security Systems. "WHAT IS A TURNSTILE? EVERYTHING YOU NEED TO KNOW". Accessed: Mar. 31, 2026. [Online]. Available: https://www.ezisecurity.com.au/what-is-a-turnstile-everything-you-need-to-know/

Motorola Solutions, Inc. "Using security turnstile gates and access control to manage crowds". Accessed: Mar. 31, 2026. [Online]. Available: https://www.avigilon.com/blog/turnstile-security

Nundlab, Inc. "Turnstiles access control systems". Accessed: Mar. 31, 2026. [Online]. Available: https://nundnet.com/turnstiles-access-control-systems/

Koorsen Fire & Security. "WHAT ARE THE DIFFERENT TYPES OF SECURITY TURNSTILES? HOW DO THEY WORK?". Accessed: Mar. 31, 2026. [Online]. Available: https://blog.koorsen.com/what-are-the-different-types-of-security-turnstiles-how-do-they-work