$(function () {
  // Filter glossary terms
  $('#glossaryFilter').on('keyup', function () {
    $('.definition').hide()
    $(`.definition:contains(${$(this).val()})`).show()
  })
});