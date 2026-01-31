import os
import re

def replace_footer(folder_path, new_footer):
    # Regex pattern: match the footer starting with your given footer class up to </footer>
    pattern = re.compile(
    r'<header\b[^>]*class="site-header"[^>]*>.*?</header>',
    re.DOTALL
)

    # Walk through all files in the folder recursively
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".html") or file.endswith(".htm"):  # Only work on HTML files
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    if pattern.search(content):
                        updated_content = pattern.sub(new_footer, content)

                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(updated_content)

                        print(f"[✔] Footer replaced in: {file_path}")
                    else:
                        print(f"[ ] Footer not found in: {file_path}")

                except Exception as e:
                    print(f"[ERROR] Could not process {file_path} -> {e}")


folder_path = r"c:\Users\Administrator\Downloads\us\us tech updated (1)"  # Fixed path

new_footer = """<header class="site-header" role="banner">
        <div class="site-header__col site-header__col--logo">
            <a href="index.html@p=2839.html" class="logo">
                <?xml version="1.0" encoding="UTF-8"?>
                <img src="./wp-content/images/us_tech_logo-removebg-preview.png" alt="">
            </a>
        </div>
        <div class="site-header__col site-header__col--mobile">
            <div class="nav-mobile-toggle hamburger hamburger--spin js-hamburger">
                <div class="hamburger-box">
                    <div class="hamburger-inner"></div>
                </div>
            </div>
        </div>
        <div class="site-header__col site-header__col--nav">
            <nav class="nav-main-wrap" role="navigation">
                <ul id="nav-main" class="nav-main nav group">
                    <li class=' menu-item menu-item-type-post_type menu-item-object-page'><a
                            href="index.html@p=486.html" target="">Services</a><button
                            class="js-sub-toggle menu-sub-toggle"><svg version="1.1" id="Layer_1"
                                xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
                                y="0px" viewBox="0 0 15.3 8" style="enable-background:new 0 0 15.3 8;"
                                xml:space="preserve">
                                <g>
                                    <path class="st0"
                                        d="M13.9,0L13.9,0L8,5.9l0,0C7.9,6,7.8,6,7.6,6C7.5,6,7.4,6,7.3,5.9l0,0L1.4,0L0,1.4l5.9,5.9l0,0C6.4,7.8,7,8,7.6,8l0,0l0,0c0.6,0,1.3-0.2,1.7-0.7l0,0l5.9-5.9L13.9,0" />
                                </g>
                            </svg></button>
                        <div class="nav__sub-menu mega-menu">
                            <div class="cotainer-fluid">
                                <div class="grid-x grid-margin-x align-justify">
                                    <div class="mega-col mega-col--1-5 mega-col-18">
                                        <style>
                                            @media screen and (min-width: 1025px) {
                                                .mega-col-18::after {
                                                    background-image: url(wp-content/uploads/2020/04/e9-supporting-cheal-85.jpg);
                                                }
                                            }
                                        </style>
                                        <div class="mega-menu__mobile-heading">Branding</div>
                                        <div class="mega-menu__heading">Branding</div>
                                        <ul class="no-style mega-menu__list">
                                            <li><a href="index.html@p=1901.html">Creative Logo Design</a></li>
                                            <li><a href="index.html@p=923.html">Brand Identity Design Services</a></li>
                                            <li><a href="index.html@p=925.html">Branding Collateral</a></li>
                                        </ul>
                                    </div>
                                    <div class="mega-col mega-col--1-5 mega-col-15">
                                        <style>
                                            @media screen and (min-width: 1025px) {
                                                .mega-col-15::after {
                                                    background-image: url(wp-content/uploads/2020/04/e9-supporting-cheal-15.jpg);
                                                }
                                            }
                                        </style>
                                        <div class="mega-menu__mobile-heading">Digital Marketing</div>
                                        <div class="mega-menu__heading">Digital Marketing</div>
                                        <ul class="no-style mega-menu__list">
                                            <li><a href="index.html@p=937.html">Digital Marketing Strategies</a></li>
                                            <li><a href="index.html@p=936.html">Social Media Marketing Services</a></li>
                                            <li><a href="service/search-engine-optimization/index.html">SEO Services
                                                </a></li>
                                            <li><a href="index.html@p=934.html">PPC Services</a></li>
                                            <li><a href="index.html@p=933.html">Data Analytics + Business Intelligence
                                                    Services</a></li>
                                            <li><a href="service/content-marketing-services/index.html">Content
                                                    Marketing Agency Services</a></li>
                                        </ul>
                                    </div>
                                    <div class="mega-col mega-col--1-5 mega-col-17">
                                        <style>
                                            @media screen and (min-width: 1025px) {
                                                .mega-col-17::after {
                                                    background-image: url(wp-content/uploads/2020/04/e9-supporting-cheal-5.jpg);
                                                }
                                            }
                                        </style>
                                        <div class="mega-menu__mobile-heading">Experience Design</div>
                                        <div class="mega-menu__heading">Experience Design</div>
                                        <ul class="no-style mega-menu__list">
                                            <li><a href="index.html@p=917.html">Information Architecture + User
                                                    Experience Design</a></li>
                                            <li><a href="index.html@p=827.html">Custom Web Design</a></li>
                                            <li><a href="service/wordpress-website-design/index.html">Wordpress Website
                                                    Design & Development Services</a></li>
                                            <li><a href="service/ada-compliance-wcag-2-1-aa/index.html">ADA Compliant
                                                    Web Design WCAG 2.1 AA </a></li>
                                            <li><a href="index.html@p=915.html">eCommerce Web Design</a></li>
                                        </ul>
                                    </div>
                                    <div class="mega-col mega-col--1-5 mega-col-14">
                                        <style>
                                            @media screen and (min-width: 1025px) {
                                                .mega-col-14::after {
                                                    background-image: url(wp-content/uploads/2020/04/e9-supporting-cheal-20.jpg);
                                                }
                                            }
                                        </style>
                                        <div class="mega-menu__mobile-heading">Strategy</div>
                                        <div class="mega-menu__heading">Strategy</div>
                                        <ul class="no-style mega-menu__list">
                                            <li><a href="index.html@p=926.html">Digital Brand Strategy</a></li>
                                            <li><a href="index.html@p=928.html">Brand Strategy Services</a></li>
                                            <li><a href="index.html@p=929.html">Digital Transformation Strategy</a></li>
                                        </ul>
                                    </div>
                                    <div class="mega-col mega-col--1-5 mega-col-16">
                                        <style>
                                            @media screen and (min-width: 1025px) {
                                                .mega-col-16::after {
                                                    background-image: url(wp-content/uploads/2020/04/e9-supporting-cheal-70.jpg);
                                                }
                                            }
                                        </style>
                                        <div class="mega-menu__mobile-heading">Technology</div>
                                        <div class="mega-menu__heading">Technology</div>
                                        <ul class="no-style mega-menu__list">
                                            <li><a href="index.html@p=924.html">Solutions Architecture</a></li>
                                            <li><a href="index.html@p=922.html">Website Development Service</a></li>
                                            <li><a href="index.html@p=921.html">App Development Service</a></li>
                                            <li><a href="index.html@p=920.html">eCommerce Website Development
                                                    Service</a></li>
                                            <li><a href="index.html@p=918.html">Web Content Management Systems</a></li>
                                        </ul>
                                    </div>

                                    <!-- hide new add  -->
                                    <div class="mega-col mega-col--1-5 mega-col-16">
                                        <style>
                                            @media screen and (min-width: 1025px) {
                                                .mega-col-16::after {
                                                    background-image: url(wp-content/uploads/2020/04/e9-supporting-cheal-70.jpg);
                                                }
                                            }
                                        </style>
                                        <div class="mega-menu__mobile-heading">Database Services
                                        </div>
                                        <div class="mega-menu__heading">Database Services
                                        </div>
                                        <ul class="no-style mega-menu__list">
                                            <li><a href="index.html@p=924 - core.html"> Our Core Database Service
                                                </a></li>
                                            <li><a href="index.html@p=924 - advanced.html"> Advanced Database Solutions
                                                </a></li>
                                            <li><a href="index.html@p=924 - Oracle.html">Oracle Exadata Services</a>
                                            </li>
                                            <!-- <li><a href="index.html@p=920.html">eCommerce Website Development
                                                    Service</a></li>
                                            <li><a href="index.html@p=918.html">Web Content Management Systems</a></li> -->
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </li>
                </ul>
                <div class="m-header-buttons">
                    <a class="m-button open-project-form-popup popmake-9506">Have a Project?</a>
                    <a class="m-button" href="partners.html">Partner with UTT</a>
                    
                    
                    <a class="m-button" style="background-color: #F3C227; border: none; color: black;" href="tel:734-771-9850">734-771-9850</a>
                    
                    <div class="m-phone-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 89.28 90.24">
                            <path
                                d="M.87,24.97C.32,15.02,14.33-4.86,19.82,3.22c.02.02.03.05.05.07l11.46,18.45c.15.25,1.25,2.33,1.3,2.62.89,4.73-3.8,9.26-7.35,14.48-.45.66-.83,1.75-.44,2.43,3.18,5.54,6.04,8.94,10.38,13.28s7.74,7.2,13.28,10.38c.69.4,1.78,0,2.43-.44,5.22-3.55,9.75-8.24,14.48-7.35.28.05,2.37,1.15,2.62,1.3l18.45,11.46s.05.03.07.05c8.09,5.5-11.8,19.51-21.75,18.95-14.41-.8-29.99-9.58-42.17-21.76C10.44,54.97,1.67,39.39.87,24.97h0Z"
                                style="fill: #f3c227; fill-rule: evenodd;" />
                        </svg>
                        <div class="m-phone-icon-dropdown">
                            <a href="tel:1646.694.0359">646.694.0359</a>
                        </div>
                    </div>
                </div>
            </nav>
        </div>
        <!--div class="site-header__col site-header__col--location">
		
        <a href="" target="_blank" class="location">
            <svg xmlns="http://www.w3.org/2000/svg" width="28.103" height="35.036" viewBox="0 0 28.103 35.036"><g transform="translate(-47.2)"><g transform="translate(47.2)"><path d="M61.244,0A14.063,14.063,0,0,0,47.2,14.044a13.823,13.823,0,0,0,.25,2.637c.007.051.037.206.1.47a13.831,13.831,0,0,0,.94,2.769c1.513,3.562,4.84,9.035,12.142,14.9a.995.995,0,0,0,1.249,0c7.294-5.861,10.628-11.334,12.142-14.9a13.676,13.676,0,0,0,.94-2.769c.059-.264.088-.419.1-.47a14.442,14.442,0,0,0,.25-2.637A14.085,14.085,0,0,0,61.244,0Zm11.84,16.336c0,.015-.007.029-.007.044-.007.037-.029.147-.066.316v.015A11.661,11.661,0,0,1,72.2,19.1c-.007.007-.007.022-.015.029-1.374,3.254-4.385,8.219-10.937,13.633-6.552-5.413-9.563-10.379-10.937-13.633-.007-.007-.007-.022-.015-.029a12.439,12.439,0,0,1-.815-2.395V16.7c-.044-.169-.059-.279-.066-.316,0-.015-.007-.029-.007-.051a12.06,12.06,0,1,1,23.681.007Z" transform="translate(-47.2)" fill="#f3c227"/><path d="M125.917,71.9a8.917,8.917,0,1,0,8.917,8.917A8.931,8.931,0,0,0,125.917,71.9Zm0,15.851a6.934,6.934,0,1,1,6.934-6.934A6.942,6.942,0,0,1,125.917,87.751Z" transform="translate(-111.873 -66.619)" fill="#f3c227"/></g></g></svg>
            New York, NY        </a>
    </div-->
    </header>"""

replace_footer(folder_path, new_footer)

