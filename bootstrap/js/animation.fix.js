$('#menuzinho').on('show.bs.collapse',function() {
		$('#logo_header').css('transform','translate(-50%,-2%)');
})

$('#menuzinho').on('hide.bs.collapse',function() {
		$('#logo_header').css('transform','translate(-50%,-50%)');
})