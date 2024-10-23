var arg1 = 'A29D63292AB18D5C8FE033DA633928F36C6E66E1';
function setCookie(name, value) {
    var expiredate = new Date();
    expiredate.setTime(expiredate.getTime() + (3600 * 1000));
    document.cookie = name + "=" + value + ";expires=" + expiredate.toGMTString() + ";max-age=3600;path=/";
}
function reload(x) {
    setCookie("acw_sc__v2", x);
    document.location.reload();
}
