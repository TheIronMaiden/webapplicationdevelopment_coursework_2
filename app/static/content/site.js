$("#filter-list-completed").on("change", function(e){

    let context = $(this);
    let list = $(".task-list-row");
    let isCompleted = context.val();

    list.each(function(e){
      console.log("isCompleted: " + isCompleted)
      let completed = $(this).attr("data-iscompleted");
      if (isCompleted == '1') {
        console.log(completed);
        if (completed == "True") {
          console.log("Showing something");
          $(this).show();
        }else{
          console.log("Hiding something");
          $(this).hide();
        }
      }else if(isCompleted == '2'){
        console.log(completed);
        if (completed == "True") {
          console.log("Hiding something");

          $(this).hide();
        }else{
          console.log("Showing something");

          $(this).show();
        }
      }else{
        $(this).show();
      }
    })
});
