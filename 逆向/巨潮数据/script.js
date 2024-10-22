
var _0x154af1 = {
  phNWP: function (_0x417158, _0x163dab) {
    return _0x417158 / _0x163dab;
  },
  lBOld: "1234567887654321",
  IBHVr: "tempenc",
};
function getResCode() {
  var _0x3d64a7 = CryptoJS["AES"]["encrypt"](
    CryptoJS["enc"]["Utf8"]["parse"](
      Math["floor"](_0x154af1["phNWP"](new Date()["getTime"](), 1000))
    ),
    CryptoJS["enc"]["Utf8"]["parse"](
     _0x154af1["lBOld"]
    ),
    {
      iv: CryptoJS["enc"]["Utf8"]["parse"](_0x154af1["lBOld"]),
      mode: CryptoJS["mode"]["CBC"],
      padding: CryptoJS["pad"]["Pkcs7"],
    }
  );
  return CryptoJS["enc"]["Base64"]["stringify"](_0x3d64a7["ciphertext"]);
}
