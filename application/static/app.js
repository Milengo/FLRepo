$().ready(
    function () {
        $.fn.filterByData = function (prop, val) {
            return this.filter(
                function () {
                    return $(this).data(prop) === val;
                }
            );
        };
        $.fn.enableFilter = function () {
            var src_lang = $('#source').val();
            var trg_lang = $('#target').val();
            var client = $('#client').val();
            alert(client);
            $("tr").show();
            $("tr").hide();
            if (src_lang !== '') {
                $("tr").filterByData('srclang', src_lang).show();
            }
            if (trg_lang !== '') {
                $("tr").filterByData('trglang', trg_lang).show();
            }
        };
        $.fn.resetFilter = function () {
            $("tr").show();
            $("#source").val = "";
            $("#target").val = "";
        };

        $("#apply_filter").click($.fn.enableFilter);
        $("#reset_filter").click($.fn.resetFilter);
    }
);