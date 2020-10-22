// Itemlists //
$(document).ready( function () {
    $('#itemlist').DataTable();
} );

$('#itemlist').DataTable( {
	"paging": false,
	"bInfo": false,
	"order": [[1, 'asc']],
	"columnDefs": [
		{ "orderable": false, "targets": [2] },
	]
} );


// Campaign Index //
$(document).ready( function () {
    $('#chapters').DataTable();
} );

$('#chapters').DataTable( {
	"paging": false,
	"bInfo": false,
	"order": [[0, 'asc']],
	"columnDefs": [
		{ "orderable": false, "targets": [1] },
	]
} );

$(document).ready( function () {
    $('#quests').DataTable();
} );

$('#quests').DataTable( {
	"paging": false,
	"bInfo": false,
	"order": [[1, 'asc']],
	"columnDefs": [
		{ "orderable": true, "targets": [0, 1, 2] },
	]
} );

$(document).ready( function () {
    $('#encounters').DataTable();
} );

$('#encounters').DataTable( {
	"paging": false,
	"bInfo": false,
	"columnDefs": [
		{ "orderable": true, "targets": [0, 1, 2] },
	]
} );

// Universe Index //

$(document).ready( function () {
    $('#empires').DataTable();
} );

$('#empires').DataTable( {
	"paging": false,
	"bInfo": false,
	"columnDefs": [
		{ "orderable": false, "targets": [1] },
	]
} );

$(document).ready( function () {
    $('#regions').DataTable();
} );

$('#regions').DataTable( {
	"paging": false,
	"bInfo": false,
	"columnDefs": [
		{ "orderable": true, "targets": [0] },
	]
} );

$(document).ready( function () {
    $('#areas').DataTable();
} );

$('#areas').DataTable( {
	"paging": false,
	"bInfo": false,
	"columnDefs": [
		{ "orderable": true, "targets": [0, 1] },
	]
} );

$(document).ready( function () {
    $('#locations').DataTable();
} );

$('#locations').DataTable( {
	"paging": false,
	"bInfo": false,
	"columnDefs": [
		{ "orderable": true, "targets": [0, 1] },
	]
} );

$(document).ready( function () {
    $('#dungeons').DataTable();
} );

$('#dungeons').DataTable( {
	"paging": false,
	"bInfo": false,
	"columnDefs": [
		{ "orderable": true, "targets": [0, 1] },
	]
} );

$(document).ready( function () {
    $('#factions').DataTable();
} );

$('#factions').DataTable( {
	"paging": false,
	"bInfo": false,
	"columnDefs": [
		{ "orderable": true, "targets": [0] },
	]
} );

$(document).ready( function () {
    $('#npcs').DataTable();
} );

$('#npcs').DataTable( {
	"paging": false,
	"bInfo": false,
	"columnDefs": [
		{ "orderable": true, "targets": [0, 1] },
	]
} );

$(document).ready( function () {
    $('#pantheons').DataTable();
} );

$('#pantheons').DataTable( {
	"paging": false,
	"bInfo": false,
	"columnDefs": [
		{ "orderable": true, "targets": [0] },
	]
} );

$(document).ready( function () {
    $('#gods').DataTable();
} );

$('#gods').DataTable( {
	"paging": false,
	"bInfo": false,
	"columnDefs": [
		{ "orderable": true, "targets": [0, 1, 2] },
	]
} );
