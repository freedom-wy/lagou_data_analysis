$(function () {
    $.ajax({
        type:'get',
        url:'/get_data',
        dataType:'json',
        success:function(returnData){
            console.log(returnData.name)
        }
    })
});
