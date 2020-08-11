/*jshint esversion: 10 */
/*jshint -W033 */

const newReviewForm = $('#newUserReview > form')
const reviewContent = $('#id_review_content')
const reviewSubmit = $('#reviewSubmitButton')
const editReview = $('#editReview')

/**
 * Enables form to add or edit review.
 */
const enableReviewForm = () => {
	reviewContent.removeAttr('disabled')
	reviewSubmit.parent().addClass('d-block')
	newReviewForm.addClass('d-block')
	editReview.attr('id', 'cancelEditReview').removeClass('far fa-edit').addClass('fas fa-times')
}

/**
 * Disables form to add or edit review.
 */
const disableReviewForm = () => {
	reviewContent.attr('disabled', 'true')
	reviewSubmit.parent().removeClass('d-block')
	newReviewForm.removeClass('d-block')
	$('#cancelEditReview').attr('id', 'editReview').removeClass('fas fa-times').addClass('far fa-edit')
}

$(document).ready(function () {
	$(document).on('click', '#editReview', function () {
		enableReviewForm()
	})
	$(document).on('click', '#cancelEditReview', function () {
		disableReviewForm()
	})
})