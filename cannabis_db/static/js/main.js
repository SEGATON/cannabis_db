$(document).ready(function(){
	$('#query_suggest').keyup(function(){
			var query = $(this).val();
			$.ajax(function(){
				type:'GET',
				url: {% url 'cannabis_db:search_results' %},
				data:{query_suggest},
				success: function(data){
					console.log('success');
					console.log(data)l;
				}
			});
	});
});