(function($)
{
    $('.show-modal-delete').click(function(e)
    {
        var action = $(this).data('action');
        var modal = $('#modal-delete');

        e.preventDefault();

        modal.find('form').attr('action', action);
        modal.modal('show');
    });
})
(jQuery);