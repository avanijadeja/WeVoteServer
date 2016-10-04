# apis_v1/urls.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-
"""
This is called from config/urls.py like this:
    url(r'^apis/v1/', include('apis_v1.urls', namespace="apis_v1")),
"""

from django.conf.urls import url
from . import views
from . import views_docs
from ballot.views_admin import BallotItemsSyncOutView, BallotReturnedSyncOutView
from candidate.views_admin import CandidatesSyncOutView
from election.views_admin import ElectionsSyncOutView
from measure.views_admin import MeasuresSyncOutView
from office.views_admin import OfficesSyncOutView
from organization.views_admin import OrganizationsSyncOutView
from polling_location.views_admin import PollingLocationsSyncOutView
from position.views_admin import PositionsSyncOutView
from voter_guide.views_admin import VoterGuidesSyncOutView

urlpatterns = [
    # Actual API Calls
    url(r'^ballotItemOptionsRetrieve/', views.ballot_item_options_retrieve_view, name='ballotItemOptionsRetrieveView'),
    url(r'^ballotItemRetrieve/', views.ballot_item_retrieve_view, name='ballotItemRetrieveView'),
    url(r'^ballotItemsSyncOut/', BallotItemsSyncOutView.as_view(), name='ballotItemsSyncOutView'),
    url(r'^ballotReturnedSyncOut/', BallotReturnedSyncOutView.as_view(), name='ballotReturnedSyncOutView'),
    url(r'^candidateRetrieve/', views.candidate_retrieve_view, name='candidateRetrieveView'),
    url(r'^candidatesRetrieve/', views.candidates_retrieve_view, name='candidatesRetrieveView'),
    url(r'^candidatesSyncOut/', CandidatesSyncOutView.as_view(), name='candidatesSyncOutView'),
    url(r'^deviceIdGenerate/$', views.device_id_generate_view, name='deviceIdGenerateView'),
    url(r'^electionsSyncOut/', ElectionsSyncOutView.as_view(), name='electionsSyncOutView'),
    url(r'^facebookDisconnect/', views.facebook_disconnect_view, name='facebookDisconnectView'),
    url(r'^facebookSignIn/', views.facebook_sign_in_view, name='facebookSignInView'),
    url(r'^friendInvitationByEmailSend/',
        views.friend_invitation_by_email_send_view, name='friendInvitationByEmailSendView'),
    url(r'^friendInvitationByEmailVerify/',
        views.friend_invitation_by_email_verify_view, name='friendInvitationByEmailVerifyView'),
    url(r'^friendInviteResponse/', views.friend_invite_response_view, name='friendInviteResponseView'),
    url(r'^friendList/', views.friend_list_view, name='friendListView'),
    url(r'^measureRetrieve/', views.measure_retrieve_view, name='measureRetrieveView'),
    url(r'^measuresSyncOut/', MeasuresSyncOutView.as_view(), name='measuresSyncOutView'),
    url(r'^officeRetrieve/', views.office_retrieve_view, name='officeRetrieveView'),
    url(r'^officesSyncOut/', OfficesSyncOutView.as_view(), name='officesSyncOutView'),
    url(r'^organizationCount/', views.organization_count_view, name='organizationCountView'),
    url(r'^organizationFollow/', views.organization_follow_api_view, name='organizationFollowView'),
    url(r'^organizationFollowIgnore/', views.organization_follow_ignore_api_view, name='organizationFollowIgnoreView'),
    url(r'^organizationRetrieve/', views.organization_retrieve_view, name='organizationRetrieveView'),
    url(r'^organizationSave/', views.organization_save_view, name='organizationSaveView'),
    url(r'^organizationSearch/', views.organization_search_view, name='organizationSearchView'),
    url(r'^organizationsSyncOut/', OrganizationsSyncOutView.as_view(), name='organizationsSyncOutView'),
    url(r'^organizationStopFollowing/',
        views.organization_stop_following_api_view, name='organizationStopFollowingView'),
    url(r'^organizationsFollowedRetrieve/',
        views.organizations_followed_retrieve_api_view, name='organizationsFollowedRetrieveView'),
    url(r'^pollingLocationsSyncOut/', PollingLocationsSyncOutView.as_view(), name='pollingLocationsSyncOutView'),
    url(r'^positionsCountForAllBallotItems/',
        views.positions_count_for_all_ballot_items_view, name='positionsCountForAllBallotItemsView'),
    url(r'^positionsCountForOneBallotItem/',
        views.positions_count_for_one_ballot_item_view, name='positionsCountForOneBallotItemView'),
    url(r'^positionLikeCount/', views.position_like_count_view, name='positionLikeCountView'),
    url(r'^positionListForBallotItem/', views.position_list_for_ballot_item_view, name='positionListForBallotItemView'),
    url(r'^positionListForOpinionMaker/',
        views.position_list_for_opinion_maker_view, name='positionListForOpinionMakerView'),
    url(r'^positionListForVoter/',
        views.position_list_for_voter_view, name='positionListForVoterView'),
    url(r'^positionOpposeCountForBallotItem/',
        views.position_oppose_count_for_ballot_item_view, name='positionOpposeCountForBallotItemView'),
    url(r'^positionPublicOpposeCountForBallotItem/',
        views.position_public_oppose_count_for_ballot_item_view, name='positionPublicOpposeCountForBallotItemView'),
    url(r'^positionPublicSupportCountForBallotItem/',
        views.position_public_support_count_for_ballot_item_view, name='positionPublicSupportCountForBallotItemView'),
    url(r'^positionRetrieve/', views.position_retrieve_view, name='positionRetrieveView'),
    url(r'^positionSave/', views.position_save_view, name='positionSaveView'),
    url(r'^positionsSyncOut/', PositionsSyncOutView.as_view(), name='positionsSyncOutView'),
    url(r'^positionSupportCountForBallotItem/',
        views.position_support_count_for_ballot_item_view, name='positionSupportCountForBallotItemView'),
    url(r'^quickInfoRetrieve/', views.quick_info_retrieve_view, name='quickInfoRetrieveView'),
    url(r'^searchAll/', views.search_all_view, name='searchAllView'),
    url(r'^twitterIdentityRetrieve/', views.twitter_identity_retrieve_view, name='twitterIdentityRetrieveView'),
    url(r'^twitterSignInStart/', views.twitter_sign_in_start_view, name='twitterSignInStartView'),
    url(r'^twitterSignInRequestAccessToken/',
        views.twitter_sign_in_request_access_token_view, name='twitterSignInRequestAccessTokenView'),
    url(r'^twitterSignInRequestVoterInfo/',
        views.twitter_sign_in_request_voter_info_view, name='twitterSignInRequestVoterInfoView'),
    url(r'^voterAddressRetrieve/', views.voter_address_retrieve_view, name='voterAddressRetrieveView'),
    url(r'^voterAddressSave/', views.voter_address_save_view, name='voterAddressSaveView'),
    url(r'^voterAllPositionsRetrieve/', views.voter_all_positions_retrieve_view, name='voterAllPositionsRetrieveView'),
    url(r'^voterAllStarsStatusRetrieve/',
        views.voter_all_stars_status_retrieve_view, name='voterAllStarsStatusRetrieveView'),
    url(r'^voterBallotItemsRetrieve/', views.voter_ballot_items_retrieve_view, name='voterBallotItemsRetrieveView'),
    url(r'^voterBallotItemsRetrieveFromGoogleCivic/',
        views.voter_ballot_items_retrieve_from_google_civic_view, name='voterBallotItemsRetrieveFromGoogleCivicView'),
    url(r'^voterCount/', views.voter_count_view, name='voterCountView'),
    url(r'^voterCreate/', views.voter_create_view, name='voterCreateView'),
    url(r'^voterEmailAddressRetrieve/', views.voter_email_address_retrieve_view, name='voterEmailAddressRetrieveView'),
    url(r'^voterEmailAddressSave/', views.voter_email_address_save_view, name='voterEmailAddressSaveView'),
    url(r'^voterEmailAddressVerify/', views.voter_email_address_verify_view, name='voterEmailAddressVerifyView'),
    url(r'^voterExport/', views.VoterExportView.as_view(), name='voterExportView'),
    url(r'^voterGuidePossibilityRetrieve/',
        views.voter_guide_possibility_retrieve_view, name='voterGuidePossibilityRetrieveView'),
    url(r'^voterGuidePossibilitySave/', views.voter_guide_possibility_save_view, name='voterGuidePossibilitySaveView'),
    url(r'^voterGuidesFollowedRetrieve/',
        views.voter_guides_followed_retrieve_view, name='voterGuidesFollowedRetrieveView'),
    url(r'^voterGuidesSyncOut/', VoterGuidesSyncOutView.as_view(), name='voterGuidesSyncOutView'),
    url(r'^voterGuidesToFollowRetrieve/',
        views.voter_guides_to_follow_retrieve_view, name='voterGuidesToFollowRetrieveView'),
    url(r'^voterLocationRetrieveFromIP/',
        views.voter_location_retrieve_from_ip_view, name='voterLocationRetrieveFromIPView'),
    url(r'^voterMergeTwoAccounts/', views.voter_merge_two_accounts_view, name='voterMergeTwoAccountsView'),
    url(r'^voterOpposingSave/', views.voter_opposing_save_view, name='voterOpposingSaveView'),
    url(r'^voterPhotoSave/', views.voter_photo_save_view, name='voterPhotoSaveView'),
    url(r'^voterPositionCommentSave/', views.voter_position_comment_save_view, name='voterPositionCommentSaveView'),
    url(r'^voterPositionLikeOffSave/', views.voter_position_like_off_save_view, name='voterPositionLikeOffSaveView'),
    url(r'^voterPositionLikeOnSave/', views.voter_position_like_on_save_view, name='voterPositionLikeOnSaveView'),
    url(r'^voterPositionLikeStatusRetrieve/',
        views.voter_position_like_status_retrieve_view, name='voterPositionLikeStatusRetrieveView'),
    url(r'^voterPositionRetrieve/', views.voter_position_retrieve_view, name='voterPositionRetrieveView'),
    url(r'^voterPositionVisibilitySave/',
        views.voter_position_visibility_save_view, name='voterPositionVisibilitySaveView'),
    url(r'^voterRetrieve/', views.voter_retrieve_view, name='voterRetrieveView'),
    url(r'^voterSignOut/', views.voter_sign_out_view, name='voterSignOutView'),
    url(r'^voterStarOffSave/', views.voter_star_off_save_view, name='voterStarOffSaveView'),
    url(r'^voterStarOnSave/', views.voter_star_on_save_view, name='voterStarOnSaveView'),
    url(r'^voterStarStatusRetrieve/', views.voter_star_status_retrieve_view, name='voterStarStatusRetrieveView'),
    url(r'^voterStopOpposingSave/', views.voter_stop_opposing_save_view, name='voterStopOpposingSaveView'),
    url(r'^voterStopSupportingSave/', views.voter_stop_supporting_save_view, name='voterStopSupportingSaveView'),
    url(r'^voterSupportingSave/', views.voter_supporting_save_view, name='voterSupportingSaveView'),
    url(r'^voterUpdate/', views.voter_update_view, name='voterUpdateView'),

    ##########################
    # API Documentation Views
    url(r'^docs/$', views_docs.apis_index_doc_view, name='apisIndex'),
    url(r'^docs/ballotItemOptionsRetrieve/$',
        views_docs.ballot_item_options_retrieve_doc_view, name='ballotItemOptionsRetrieveDocs'),
    url(r'^docs/ballotItemRetrieve/$', views_docs.ballot_item_retrieve_doc_view, name='ballotItemRetrieveDocs'),
    url(r'^docs/ballotItemsSyncOut/$', views_docs.ballot_items_sync_out_doc_view, name='ballotItemsSyncOutDocs'),
    url(r'^docs/ballotReturnedSyncOut/$',
        views_docs.ballot_returned_sync_out_doc_view, name='ballotReturnedSyncOutDocs'),
    url(r'^docs/candidateRetrieve/$', views_docs.candidate_retrieve_doc_view, name='candidateRetrieveDocs'),
    url(r'^docs/candidatesRetrieve/$', views_docs.candidates_retrieve_doc_view, name='candidatesRetrieveDocs'),
    url(r'^docs/candidatesSyncOut/$', views_docs.candidates_sync_out_doc_view, name='candidatesSyncOutDocs'),
    url(r'^docs/deviceIdGenerate/$', views_docs.device_id_generate_doc_view, name='deviceIdGenerateDocs'),
    url(r'^docs/electionsSyncOut/$', views_docs.elections_sync_out_doc_view, name='electionsSyncOutDocs'),
    url(r'^docs/facebookDisconnect/$', views_docs.facebook_disconnect_doc_view, name='facebookDisconnectDocs'),
    url(r'^docs/facebookSignIn/$', views_docs.facebook_sign_in_doc_view, name='facebookSignInDocs'),
    url(r'^docs/friendInvitationByEmailSend/$',
        views_docs.friend_invitation_by_email_send_doc_view, name='friendInvitationByEmailSendDocs'),
    url(r'^docs/friendInvitationByEmailVerify/$',
        views_docs.friend_invitation_by_email_verify_doc_view, name='friendInvitationByEmailVerifyDocs'),
    url(r'^docs/friendInviteResponse/$', views_docs.friend_invite_response_doc_view, name='friendInviteResponseDocs'),
    url(r'^docs/friendList/$', views_docs.friend_list_doc_view, name='friendListDocs'),
    url(r'^docs/measureRetrieve/$', views_docs.measure_retrieve_doc_view, name='measureRetrieveDocs'),
    url(r'^docs/measuresSyncOut/$', views_docs.measures_sync_out_doc_view, name='measuresSyncOutDocs'),
    url(r'^docs/officeRetrieve/$', views_docs.office_retrieve_doc_view, name='officeRetrieveDocs'),
    url(r'^docs/officeSyncOut/$', views_docs.offices_sync_out_doc_view, name='officesSyncOutDocs'),
    url(r'^docs/organizationCount/$', views_docs.organization_count_doc_view, name='organizationCountDocs'),
    url(r'^docs/organizationFollow/', views_docs.organization_follow_doc_view, name='organizationFollowDocs'),
    url(r'^docs/organizationFollowIgnore/',
        views_docs.organization_follow_ignore_doc_view, name='organizationFollowIgnoreDocs'),
    url(r'^docs/organizationRetrieve/$', views_docs.organization_retrieve_doc_view, name='organizationRetrieveDocs'),
    url(r'^docs/organizationSave/$', views_docs.organization_save_doc_view, name='organizationSaveDocs'),
    url(r'^docs/organizationSearch/$', views_docs.organization_search_doc_view, name='organizationSearchDocs'),
    url(r'^docs/organizationsSyncOut/$', views_docs.organizations_sync_out_doc_view, name='organizationsSyncOutDocs'),
    url(r'^docs/organizationStopFollowing/',
        views_docs.organization_stop_following_doc_view, name='organizationStopFollowingDocs'),
    url(r'^docs/organizationsFollowedRetrieve/',
        views_docs.organizations_followed_retrieve_doc_view, name='organizationsFollowedRetrieveDocs'),
    url(r'^docs/pollingLocationsSyncOut/$',
        views_docs.polling_locations_sync_out_doc_view, name='pollingLocationsSyncOutDocs'),
    url(r'^docs/positionLikeCount/$', views_docs.position_like_count_doc_view, name='positionLikeCountDocs'),
    url(r'^docs/positionListForBallotItem/',
        views_docs.position_list_for_ballot_item_doc_view, name='positionListForBallotItemDocs'),
    url(r'^docs/positionListForOpinionMaker/',
        views_docs.position_list_for_opinion_maker_doc_view, name='positionListForOpinionMakerDocs'),
    url(r'^docs/positionListForVoter/',
        views_docs.position_list_for_voter_doc_view, name='positionListForVoterDocs'),
    url(r'^docs/positionOpposeCountForBallotItem/',
        views_docs.position_oppose_count_for_ballot_item_doc_view, name='positionOpposeCountForBallotItemDocs'),
    url(r'^docs/positionPublicOpposeCountForBallotItem/',
        views_docs.position_public_oppose_count_for_ballot_item_doc_view,
        name='positionPublicOpposeCountForBallotItemDocs'),
    url(r'^docs/positionPublicSupportCountForBallotItem/',
        views_docs.position_public_support_count_for_ballot_item_doc_view,
        name='positionPublicSupportCountForBallotItemDocs'),
    url(r'^docs/positionRetrieve/$', views_docs.position_retrieve_doc_view, name='positionRetrieveDocs'),
    url(r'^docs/positionSave/$', views_docs.position_save_doc_view, name='positionSaveDocs'),
    url(r'^docs/positionsCountForAllBallotItemsDocs/$',
        views_docs.positions_count_for_all_ballot_items_doc_view, name='positionsCountForAllBallotItemsDocs'),
    url(r'^docs/positionsCountForOneBallotItemDocs/$',
        views_docs.positions_count_for_one_ballot_item_doc_view, name='positionsCountForOneBallotItemDocs'),
    url(r'^docs/positionsSyncOut/$', views_docs.positions_sync_out_doc_view, name='positionsSyncOutDocs'),
    url(r'^docs/positionSupportCountForBallotItem/',
        views_docs.position_support_count_for_ballot_item_doc_view, name='positionSupportCountForBallotItemDocs'),
    url(r'^docs/quickInfoRetrieve/$', views_docs.quick_info_retrieve_doc_view, name='quickInfoRetrieveDocs'),
    url(r'^docs/searchAll/$',
        views_docs.search_all_doc_view, name='searchAllDocs'),
    url(r'^docs/twitterIdentityRetrieve/$',
        views_docs.twitter_identity_retrieve_doc_view, name='twitterIdentityRetrieveDocs'),
    url(r'^docs/twitterSignInStart/$', views_docs.twitter_sign_in_start_doc_view, name='twitterSignInStartDocs'),
    url(r'^docs/twitterSignInRequestAccessToken/$',
        views_docs.twitter_sign_in_request_access_token_doc_view, name='twitterSignInRequestAccessTokenDocs'),
    url(r'^docs/twitterSignInRequestVoterInfo/$',
        views_docs.twitter_sign_in_request_voter_info_doc_view, name='twitterSignInRequestVoterInfoDocs'),
    url(r'^docs/voterAddressRetrieve/$', views_docs.voter_address_retrieve_doc_view, name='voterAddressRetrieveDocs'),
    url(r'^docs/voterAddressSave/$', views_docs.voter_address_save_doc_view, name='voterAddressSaveDocs'),
    url(r'^docs/voterAllPositionsRetrieve/$',
        views_docs.voter_all_positions_retrieve_doc_view, name='voterAllPositionsRetrieveDocs'),
    url(r'^docs/voterAllStarsStatusRetrieve/$',
        views_docs.voter_all_stars_status_retrieve_doc_view, name='voterAllStarsStatusRetrieveDocs'),
    url(r'^docs/voterBallotItemsRetrieve/$',
        views_docs.voter_ballot_items_retrieve_doc_view, name='voterBallotItemsRetrieveDocs'),
    url(r'^docs/voterBallotItemsRetrieveFromGoogleCivic/$',
        views_docs.voter_ballot_items_retrieve_from_google_civic_doc_view,
        name='voterBallotItemsRetrieveFromGoogleCivicDocs'),
    url(r'^docs/voterCount/$', views_docs.voter_count_doc_view, name='voterCountDocs'),
    url(r'^docs/voterCreate/$', views_docs.voter_create_doc_view, name='voterCreateDocs'),
    url(r'^docs/voterEmailAddressRetrieve/$',
        views_docs.voter_email_address_retrieve_doc_view, name='voterEmailAddressRetrieveDocs'),
    url(r'^docs/voterEmailAddressSave/$',
        views_docs.voter_email_address_save_doc_view, name='voterEmailAddressSaveDocs'),
    url(r'^docs/voterEmailAddressVerify/$',
        views_docs.voter_email_address_verify_doc_view, name='voterEmailAddressVerifyDocs'),
    url(r'^docs/voterGuidePossibilityRetrieve/$',
        views_docs.voter_guide_possibility_retrieve_doc_view, name='voterGuidePossibilityRetrieveDocs'),
    url(r'^docs/voterGuidePossibilitySave/$',
        views_docs.voter_guide_possibility_save_doc_view, name='voterGuidePossibilitySaveDocs'),
    url(r'^docs/voterGuidesToFollowRetrieve/$',
        views_docs.voter_guides_to_follow_retrieve_doc_view, name='voterGuidesToFollowRetrieveDocs'),
    url(r'^docs/voterGuidesFollowedRetrieve/$',
        views_docs.voter_guides_followed_retrieve_doc_view, name='voterGuidesFollowedRetrieveDocs'),
    url(r'^docs/voterGuidesSyncOut/$', views_docs.voter_guides_sync_out_doc_view, name='voterGuidesSyncOutDocs'),
    url(r'^docs/voterLocationRetrieveFromIP/$',
        views_docs.voter_location_retrieve_from_ip_doc_view, name='voterLocationRetrieveFromIPDocs'),
    url(r'^docs/voterMergeTwoAccounts/$',
        views_docs.voter_merge_two_accounts_doc_view, name='voterMergeTwoAccountsDocs'),
    url(r'^docs/voterPhotoSave/$', views_docs.voter_photo_save_doc_view, name='voterPhotoSaveDocs'),
    url(r'^docs/voterOpposingSave/$', views_docs.voter_opposing_save_doc_view, name='voterOpposingSaveDocs'),
    url(r'^docs/voterPositionRetrieve/$',
        views_docs.voter_position_retrieve_doc_view, name='voterPositionRetrieveDocs'),
    url(r'^docs/voterPositionCommentSave/$',
        views_docs.voter_position_comment_save_doc_view, name='voterPositionCommentSaveDocs'),
    url(r'^docs/voterPositionLikeOffSave/$',
        views_docs.voter_position_like_off_save_doc_view, name='voterPositionLikeOffSaveDocs'),
    url(r'^docs/voterPositionLikeOnSave/$',
        views_docs.voter_position_like_on_save_doc_view, name='voterPositionLikeOnSaveDocs'),
    url(r'^docs/voterPositionLikeStatusRetrieve/$',
        views_docs.voter_position_like_status_retrieve_doc_view, name='voterPositionLikeStatusRetrieveDocs'),
    url(r'^docs/voterPositionVisibilitySave/$',
        views_docs.voter_position_visibility_save_doc_view, name='voterPositionVisibilitySaveDocs'),
    url(r'^docs/voterRetrieve/$', views_docs.voter_retrieve_doc_view, name='voterRetrieveDocs'),
    url(r'^docs/voterSignOut/$', views_docs.voter_sign_out_doc_view, name='voterSignOutDocs'),
    url(r'^docs/voterStarOffSave/$', views_docs.voter_star_off_save_doc_view, name='voterStarOffSaveDocs'),
    url(r'^docs/voterStarOnSave/$', views_docs.voter_star_on_save_doc_view, name='voterStarOnSaveDocs'),
    url(r'^docs/voterStarStatusRetrieve/$',
        views_docs.voter_star_status_retrieve_doc_view, name='voterStarStatusRetrieveDocs'),
    url(r'^docs/voterStopOpposingSave/$',
        views_docs.voter_stop_opposing_save_doc_view, name='voterStopOpposingSaveDocs'),
    url(r'^docs/voterStopSupportingSave/$',
        views_docs.voter_stop_supporting_save_doc_view, name='voterStopSupportingSaveDocs'),
    url(r'^docs/voterSupportingSave/$', views_docs.voter_supporting_save_doc_view, name='voterSupportingSaveDocs'),
    url(r'^docs/voterUpdate/$', views_docs.voter_update_doc_view, name='voterUpdateDocs'),
]
