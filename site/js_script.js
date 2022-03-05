function getVal() {
var inputText = document.getElementById("vk_URL").value;
var inputBrief = inputText.replace('https://vk.com/away.php?to=', '');
var inputBrief2 = inputBrief.replace('%3A', ':');
var output = inputBrief2.replaceAll('%2F', '/');
document.getElementById('normal_URL').value = output;
}

function goToNewPage()
    {
        var url = document.getElementById('list').value;
        if(url != 'none') {
            window.open(value, "_self")
        }
    }
// https://vk.com/away.php?to=https%3A%2F%2Fgist.github.com%2Fshahwan42%2F279f6ec17dfc91ec9c6f778ae2877b2d
