
var seconds = 23;
var minutes = 34;
var hours = 12;
var days = 80;
var flag = 0

function seetup()
{
    console.log("hey")
    var sec = document.getElementById('Second');
    var min = document.getElementById('Minute');
    var hou = document.getElementById('Hour');
    var day = document.getElementById('Days');

    sec.innerText = '0';

    console.log(sec);

    function dayIt()
    {
        if(flag == 0)
        days--;
        if(days == -1)
        {
           seconds = 0;
           minutes = 0;
           hours = 0;
           days = 0;
           flag = 1;
        }
        day.innerText = days + "D :";
    }

    function houIt()
    {
        if(flag == 0)
        hours--;
        if(hours == -1)
        {
            hours = 23;
            dayIt();
        }
        hou.innerText = hours + "H :";
    }

    function minIt()
    {
        if(flag == 0)
        minutes--;
        if(minutes==-1)
        {
            minutes = 59;
            houIt();
        }
        min.innerText = minutes + "M :";
    }

    function secIt()
    {
        if(flag == 0)
        seconds--;
        if(seconds==-1)
        {
            seconds = 59;
            minIt();
        }
       sec.innerText = seconds + "S";
    }

    // native java script function
    if(flag == 0)
    setInterval(secIt, 1000);
}