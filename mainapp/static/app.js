$( document ).ready(function() {
    $(".chosen").data("placeholder","Select Language").chosen();
    $("#srclang").change(function(){
    	var result = $(this).val();
    	if (result == null) {
    		$("[data-srclang]").show();
    		$("#trglang").change();
    		return;
    		}
    	else{
    	$('[data-srclang]').hide();
    	$.each($('#srclang').val(), function(index, value){$(CH.formatString('[data-srclang={1}', value)).show();});
    	}
    });
    $("#trglang").change(function(){
    	var result = $(this).val();
    	if (result == null) {
    		$("[data-trglang]").show();
    		$("#srclang").change();
    		return;
    	}
    	else{
    		$('[data-trglang]').hide();
    		$.each($('#trglang').val(), function(index, value){$(CH.formatString('[data-trglang={1}', value)).show();});
    	}
    });
});

var CH = {};
CH = {
formatString: function()
    {
        var args = [].slice.call(arguments);
        if(this.toString() != '[object Object]')
        {
            args.unshift(this.toString());
        }
 
        var pattern = new RegExp('{([1-' + args.length + '])}','g');
        return String(args[0]).replace(pattern, function(match, index) { return args[index]; });
    }
}
