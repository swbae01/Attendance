function LoadLecture() {

    // Toggle button hide...
    $("#navbarNav").collapse('hide');

    $("#mainBase").load("/static/myapp/lecture_list.html", function(responseTxt, statusTxt, xhr){
        if(statusTxt === "error") {
            alert("error");
            return;
        }
        
    }); 
}