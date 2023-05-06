$("document").ready(function () {
	$("input#btn_translate").click(translate);
	$("input#language_code").focus(function () {
		$(this).keydown(function (e) {
			if (e.keyCode === 13) {
				translate();
			}
		});
	});
});

function translate() {
	const url = "https://hellosalut.stefanbohacek.dev/?";
	// const url = "https://www.fourtonfish.com/hellosalut/?";
	// const url = "https://hellosalut.stefanbohacek.dev/?lang=ja";
	$.get(
		url + $.param({ lang: $("input#language_code").val() }),
		// url,
		function (data) {
			$("DIV#hello").html(data.hello);
		}
	);
}
