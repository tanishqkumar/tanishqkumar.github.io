// Populate all states.
var states = {
    AL: [false, "Alabama"],	
    AK: [true, "Alaska"],	
    AZ: [true, "Arizona"],	
    AR: [false, "Arkansas"],	
    CA: [true, "California"],	
    CO: [true, "Colorado"],	
    CT: [true, "Connecticut"],	
    DE: [false, "Delaware"],	
    FL: [true, "Florida"],	
    GA: [true, "Georgia"],	
    HI: [true, "Hawaii"],	
    ID: [true, "Idaho"],	
    IL: [true, "Illinois"],	
    IN: [true, "Indiana"],	
    IA: [false, "Iowa"],	
    KS: [false, "Kansas"],	
    KY: [false, "Kentucky"],	
    LA: [false, "Louisiana"],	
    ME: [false, "Maine"],	
    MD: [true, "Maryland"],	
    MA: [true, "Massachusetts"],	
    MI: [true, "Michigan"],	
    MN: [false, "Minnesota"],	
    MS: [false, "Mississippi"],	
    MO: [true, "Missouri"],	
    MT: [true, "Montana"],	
    NE: [false, "Nebraska"],	
    NV: [false, "Nevada"],	
    NH: [false, "New Hampshire"],	
    NJ: [true, "New Jersey"],	
    NM: [false, "New Mexico"],	
    NY: [true, "New York"],	
    NC: [false, "North Carolina"],	
    ND: [false, "North Dakota"],	
    OH: [false, "Ohio"],	
    OK: [false, "Oklahoma"],	
    OR: [false, "Oregon"],	
    PA: [true, "Pennsylvania"],	
    RI: [false, "Rhode Island"],	
    SC: [false, "South Carolina"],	
    SD: [false, "South Dakota"],	
    TN: [false, "Tennessee"],	
    TX: [false, "Texas"],	
    UT: [true, "Utah"],	
    VT: [false, "Vermont"],	
    VA: [false, "Virginia"],	
    WA: [true, "Washington"],	
    WV: [false, "West Virginia"],	
    WI: [true, "Wisconsin"],	
    WY: [true, "Wyoming"],	
};

var statesElement = document.getElementById("states");
var keys = Object.keys(states);
var statesVisited = 0;
for (var i = 0; i < keys.length; i ++) {
    var filename = "images/SVG/states/" + keys[i] + ".svg";
    var newDiv = document.createElement('div');
    newDiv.className = "column";
    var newImg = document.createElement('img');
    newImg.src = filename;
    newImg.setAttribute("height", "100px");
    if (states[keys[i]][0]) {
        statesVisited += 1;
    } else {
        newImg.className = "not-visited";
    }
    newDiv.appendChild(newImg)
    var innerDiv = document.createElement('div');
    innerDiv.innerHTML = states[keys[i]][1];
    innerDiv.className = "label";
    newDiv.appendChild(innerDiv);
    statesElement.appendChild(newDiv);
}

// Populate total visited states.
var statesHeader = document.getElementById("visited-percentage-states");
statesHeader.innerHTML = statesVisited + "/" + keys.length;
var statesProgress = document.createElement('progress');
statesProgress.value = statesVisited;
statesProgress.max = keys.length;
statesHeader.appendChild(statesProgress);



var countries = {
    AF:	[false, "Afghanistan"],
    AX:	[false, "Aland Islands"],
    AL:	[false, "Albania"],
    DZ:	[false, "Algeria"],
    AS:	[false, "American Samoa"],
    AD:	[false, "Andorra"],
    AO:	[false, "Angola"],
    AI:	[false, "Anguilla"],
    AQ:	[false, "Antarctica"],
    AG:	[false, "Antigua and Barbuda"],
    AR:	[false, "Argentina"],
    AM:	[false, "Armenia"],
    AW:	[false, "Aruba"],
    AU:	[false, "Australia"],
    AT:	[false, "Austria"],
    AZ:	[false, "Azerbaijan"],
    BS:	[false, "Bahamas"],
    BH:	[false, "Bahrain"],
    BD:	[false, "Bangladesh"],
    BB:	[false, "Barbados"],
    BY:	[false, "Belarus"],
    BE:	[false, "Belgium"],
    BZ:	[false, "Belize"],
    BJ:	[false, "Benin"],
    BM:	[false, "Bermuda"],
    BT:	[false, "Bhutan"],
    BO:	[false, "Bolivia"],
    BQ:	[false, "Bonaire, Sint Eustatius and Saba"],
    BA:	[false, "Bosnia and Herzegovina"],
    BW:	[false, "Botswana"],
    BV:	[false, "Bouvet Island"],
    BR:	[false, "Brazil"],
    IO:	[false, "British Indian Ocean Territory"],
    BN:	[false, "Brunei"],
    BG:	[false, "Bulgaria"],
    BF:	[false, "Burkina Faso"],
    BI:	[false, "Burundi"],
    KH:	[false, "Cambodia"],
    CM:	[false, "Cameroon"],
    CA:	[true, "Canada"],
    CV:	[false, "Cape Verde"],
    KY:	[false, "Cayman Islands"],
    CF:	[false, "Central African Republic"],
    TD:	[false, "Chad"],
    CL:	[false, "Chile"],
    CN:	[false, "China"],
    CX:	[false, "Christmas Island"],
    CC:	[false, "Cocos (Keeling) Islands"],
    CO:	[false, "Colombia"],
    KM:	[false, "Comoros"],
    CG:	[false, "Congo"],
    CD:	[false, "Congo"],
    CK:	[false, "Cook Islands"],
    CR:	[false, "Costa Rica"],
    CI:	[false, "Cote d'Ivoire"],
    HR:	[false, "Croatia"],
    CU:	[false, "Cuba"],
    CW:	[false, "Curacao"],
    CY:	[false, "Cyprus"],
    CZ:	[true, "Czechia"],
    DK:	[false, "Denmark"],
    DJ:	[false, "Djibouti"],
    DM:	[false, "Dominica"],
    DO:	[false, "Dominican Republic"],
    EC:	[false, "Ecuador"],
    EG:	[false, "Egypt"],
    SV:	[false, "El Salvador"],
    GQ:	[false, "Equatorial Guinea"],
    ER:	[false, "Eritrea"],
    EE:	[false, "Estonia"],
    ET:	[false, "Ethiopia"],
    FK:	[false, "Falkland Islands (Malvinas)"],
    FO:	[false, "Faroe Islands"],
    FJ:	[false, "Fiji"],
    FI:	[false, "Finland"],
    FR:	[true, "France"],
    GF:	[false, "French Guiana"],
    PF:	[false, "French Polynesia"],
    TF:	[false, "French Southern Territories"],
    GA:	[false, "Gabon"],
    GM:	[false, "Gambia"],
    GE:	[false, "Georgia"],
    DE:	[true, "Germany"],
    GH:	[false, "Ghana"],
    GI:	[false, "Gibraltar"],
    GR:	[false, "Greece"],
    GL:	[false, "Greenland"],
    GD:	[false, "Grenada"],
    GP:	[false, "Guadeloupe"],
    GU:	[false, "Guam"],
    GT:	[false, "Guatemala"],
    GG:	[false, "Guernsey"],
    GN:	[false, "Guinea"],
    GW:	[false, "Guinea-Bissau"],
    GY:	[false, "Guyana"],
    HT:	[false, "Haiti"],
    HM:	[false, "Heard and Mc Donald Islands"],
    VA:	[false, "Vatican"],
    HN:	[false, "Honduras"],
    HK:	[true, "Hong Kong"],
    HU:	[false, "Hungary"],
    IS:	[false, "Iceland"],
    IN:	[true, "India"],
    ID:	[false, "Indonesia"],
    IR:	[false, "Iran"],
    IQ:	[false, "Iraq"],
    IE:	[false, "Ireland"],
    IM:	[false, "Isle of Man"],
    IL:	[false, "Israel"],
    IT:	[false, "Italy"],
    JM:	[false, "Jamaica"],
    JP:	[false, "Japan"],
    JO:	[false, "Jordan"],
    KZ:	[false, "Kazakstan"],
    KE:	[false, "Kenya"],
    KI:	[false, "Kiribati"],
    KP:	[true, "South Korea"],
    KR:	[false, "North Korea"],
    KW:	[false, "Kuwait"],
    KG:	[false, "Kyrgyzstan"],
    LA:	[false, "Laos"],
    LV:	[false, "Latvia"],
    LB:	[false, "Lebanon"],
    LS:	[false, "Lesotho"],
    LR:	[false, "Liberia"],
    LY:	[false, "Libyan Arab Jamahiriya"],
    LI:	[false, "Liechtenstein"],
    LT:	[false, "Lithuania"],
    LU:	[false, "Luxembourg"],
    MO:	[false, "Macao"],
    MK:	[false, "Macedonia"],
    MG:	[false, "Madagascar"],
    MW:	[false, "Malawi"],
    MY:	[false, "Malaysia"],
    MV:	[false, "Maldives"],
    ML:	[false, "Mali"],
    MT:	[false, "Malta"],
    MQ:	[false, "Martinique"],
    MR:	[false, "Mauritania"],
    MU:	[false, "Mauritius"],
    YT:	[false, "Mayotte"],
    MX:	[true, "Mexico"],
    MD:	[false, "Moldova"],
    MC:	[false, "Monaco"],
    MN:	[false, "Mongolia"],
    ME:	[false, "Montenegro"],
    MS:	[false, "Montserrat"],
    MA:	[false, "Morocco"],
    MZ:	[false, "Mozambique"],
    MM:	[false, "Myanmar"],
    NA:	[false, "Namibia"],
    NR:	[false, "Nauru"],
    NP:	[false, "Nepal"],
    NL:	[false, "Netherlands"],
    NC:	[false, "New Caledonia"],
    NZ:	[false, "New Zealand"],
    NI:	[false, "Nicaragua"],
    NE:	[false, "Niger"],
    NG:	[false, "Nigeria"],
    NU:	[false, "Niue"],
    NF:	[false, "Norfolk Island"],
    NO:	[false, "Norway"],
    OM:	[false, "Oman"],
    PK:	[false, "Pakistan"],
    PW:	[false, "Palau"],
    PA:	[false, "Panama"],
    PG:	[false, "Papua New Guinea"],
    PY:	[false, "Paraguay"],
    PE:	[true, "Peru"],
    PH:	[false, "Philippines"],
    PN:	[false, "Pitcairn"],
    PL:	[false, "Poland"],
    PT:	[false, "Portugal"],
    PR:	[true, "Puerto Rico"],
    QA:	[false, "Qatar"],
    RS:	[false, "Republic of Serbia"],
    RE:	[false, "Reunion"],
    RO:	[false, "Romania"],
    RU:	[false, "Russia"],
    RW:	[false, "Rwanda"],
    BL:	[false, "Saint Barthélemy"],
    SH:	[false, "Saint Helena"],
    KN:	[false, "Saint Kitts & Nevis"],
    LC:	[false, "Saint Lucia"],
    MF:	[false, "Saint Martin"],
    PM:	[false, "Saint Pierre and Miquelon"],
    VC:	[false, "Saint Vincent and the Grenadines"],
    WS:	[false, "Samoa"],
    SM:	[false, "San Marino"],
    ST:	[false, "Sao Tome and Principe"],
    SA:	[false, "Saudi Arabia"],
    SN:	[false, "Senegal"],
    SC:	[false, "Seychelles"],
    SL:	[false, "Sierra Leone"],
    SG:	[false, "Singapore"],
    SX:	[false, "Sint Maarten"],
    SK:	[false, "Slovakia"],
    SI:	[false, "Slovenia"],
    SB:	[false, "Solomon Islands"],
    SO:	[false, "Somalia"],
    ZA:	[false, "South Africa"],
    GS:	[false, "South Georgia & The South Sandwich Islands"],
    SS:	[false, "South Sudan"],
    ES:	[false, "Spain"],
    LK:	[false, "Sri Lanka"],
    SD:	[false, "Sudan"],
    SR:	[false, "Suriname"],
    SJ:	[false, "Svalbard and Jan Mayen"],
    SZ:	[false, "Swaziland"],
    SE:	[false, "Sweden"],
    CH:	[false, "Switzerland"],
    SY:	[false, "Syria"],
    TW:	[true, "Taiwan"],
    TJ:	[false, "Tajikistan"],
    TZ:	[false, "Tanzania"],
    TH:	[false, "Thailand"],
    TL:	[false, "Timor-Leste"],
    TG:	[false, "Togo"],
    TK:	[false, "Tokelau"],
    TO:	[false, "Tonga"],
    TT:	[false, "Trinidad and Tobago"],
    TN:	[false, "Tunisia"],
    TR:	[false, "Turkey"],
    TM:	[false, "Turkmenistan"],
    TC:	[false, "Turks and Caicos Islands"],
    UG:	[false, "Uganda"],
    UA:	[false, "Ukraine"],
    AE:	[true, "United Arab Emirates"],
    GB:	[true, "United Kingdom"],
    US:	[true, "United States"],
    UY:	[false, "Uruguay"],
    UZ:	[false, "Uzbekistan"],
    VU:	[false, "Vanuatu"],
    VE:	[false, "Venezuela"],
    VN:	[false, "Vietnam"],
    VG:	[false, "Virgin Islands, British"],
    VI:	[false, "Virgin Islands, U.S."],
    WF:	[false, "Wallis and Futuna"],
    EH:	[false, "Western Sahara"],
    YE:	[false, "Yemen"],
    ZM:	[false, "Zambia"],
    ZW:	[false, "Zimbabwe"],
};


var countriesElement = document.getElementById("countries");
var keys = Object.keys(countries);
var countriesVisited = 0;
for (var i = 0; i < keys.length; i ++) {
    var filename = "images/SVG/countries/" + keys[i] + ".svg";
    var newDiv = document.createElement('div');
    newDiv.className = "column";
    var newImg = document.createElement('img');
    newImg.src = filename;
    newImg.setAttribute("height", "100px");
    if (countries[keys[i]][0]) {
        countriesVisited += 1;
    } else {
        newImg.className = "not-visited";
    }
    newDiv.appendChild(newImg)
    var innerDiv = document.createElement('div');
    innerDiv.innerHTML = countries[keys[i]][1];
    innerDiv.className = "label";
    newDiv.appendChild(innerDiv);
    countriesElement.appendChild(newDiv);
}

// Populate total visited states.
var countriesHeader = document.getElementById("visited-percentage-world");
countriesHeader.innerHTML = countriesVisited + "/" + keys.length;
var countriesProgress = document.createElement('progress');
countriesProgress.value = countriesVisited;
countriesProgress.max = keys.length;
countriesHeader.appendChild(countriesProgress);


// Populate collabsibles.
var coll = document.getElementsByClassName("collapsible");
console.log(coll);
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}