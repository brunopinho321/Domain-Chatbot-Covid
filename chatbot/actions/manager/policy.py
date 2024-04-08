def policy(state_of_world):
    if (('goal' in state_of_world)):
        return 'goal'
    if (('can-finish-service' in state_of_world) and not('goal' in state_of_world)):
        return 'finish-service'
    if (not('can-go-error-treatment' in state_of_world) and ('can-show-ask-user-grade' in state_of_world) and not('goal' in state_of_world)):
        return 'ask-user-grade'
    if (('can-go-error-treatment' in state_of_world) and ('can-show-ask-user-grade' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('can-do-show-info-diagnostic-negative' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-diagnostic-negative'
    if (('can-do-human-take-control-dialog' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'health-agent-takes-control'
    if (('can-call-health-agent' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'call-health-agent'
    if (not('have-patient-phone-number' in state_of_world) and ('can-do-ask-patient-info-phone-number' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'ask-patient-info-phone-number'
    if (not('have-patient-phone-number' in state_of_world) and ('can-do-ask-patient-info-phone-number' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (not('have-patient-phone-number' in state_of_world) and ('have-patient-gender-f' in state_of_world) and ('can-do-ask-patient-info-pregnant-woman' in state_of_world) and not('have-patient-pregnant-info' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'ask-patient-info-pregmant-woman'
    if (not('have-patient-phone-number' in state_of_world) and ('have-patient-gender-f' in state_of_world) and ('can-do-ask-patient-info-pregnant-woman' in state_of_world) and not('have-patient-pregnant-info' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('can-show-info-others' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-others'
    if (('started' in state_of_world) and not('can-go-error-treatment' in state_of_world) and ('can-do-start-dialog' in state_of_world) and not('goal' in state_of_world)):
        return 'start-dialog'
    if (('can-show-info-others' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('have-patient-days-symptoms' in state_of_world) and ('have-patient-symptoms' in state_of_world) and not('have-diagnostic-system-positive' in state_of_world) and ('can-call-diagnostic-system' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'call-diagnostic-system'
    if (('started' in state_of_world) and not('have-patient-days-symptoms' in state_of_world) and not('have-patient-symptoms' in state_of_world) and not('have-diagnostic-system-positive' in state_of_world) and not('can-go-error-treatment' in state_of_world) and ('can-do-start-dialog' in state_of_world) and not('goal' in state_of_world)):
        return 'start-dialog'
    if (not('have-patient-phone-number' in state_of_world) and not('have-patient-comorbidities' in state_of_world) and not('have-patient-birthday' in state_of_world) and not('have-patient-name' in state_of_world) and not('have-patient-cpf' in state_of_world) and ('have-patient-days-symptoms' in state_of_world) and ('have-patient-symptoms' in state_of_world) and not('have-diagnostic-system-positive' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-gender' in state_of_world) and ('can-call-diagnostic-system' in state_of_world) and not('have-patient-location' in state_of_world) and not('have-patient-postal-code' in state_of_world) and not('can-do-ask-postal-code' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'call-diagnostic-system'
    if (('user-initiative' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-welcome-message'
    if (('started' in state_of_world) and ('can-go-error-treatment' in state_of_world) and ('can-do-start-dialog' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-mental-health' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('can-back-dialog' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-mental-health'
    if (('started' in state_of_world) and not('can-go-error-treatment' in state_of_world) and ('can-show-info-about-covid' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-covid'
    if (('started' in state_of_world) and ('can-show-info-covid-ce' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-covid-in-ceara'
    if (('started' in state_of_world) and not('can-go-error-treatment' in state_of_world) and ('can-show-info-myths-truths-covid' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-myths-and-truths'
    if (('started' in state_of_world) and ('can-show-info-about-the-restrictions-to-buy' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-the-restrictions-to-buy'
    if (('started' in state_of_world) and ('can-show-info-about-covid-kill' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-covid-kill'
    if (('started' in state_of_world) and ('can-show-info-about-covid-survive-in-surface' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-covid-survive-in-surface'
    if (('started' in state_of_world) and ('can-show-info-about-medicine-for-covid' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-medicine-for-covid'
    if (('started' in state_of_world) and ('can-show-info-about-antibiotics-effects' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-antibiotics-effects'
    if (('started' in state_of_world) and ('can-show-info-about-people-affected-by-covid' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-people-affected-by-covid'
    if (('started' in state_of_world) and ('can-show-info-about-pets-spread-covid' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('can-back-dialog' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-pets-spread-covid'
    if (('started' in state_of_world) and not('can-go-error-treatment' in state_of_world) and ('can-show-info-myths-truths-covid' in state_of_world) and not('can-back-dialog' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-myths-and-truths'
    if (('started' in state_of_world) and not('can-go-error-treatment' in state_of_world) and ('can-show-info-when-feel-symptoms' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-when-feel-the-symptoms'
    if (('started' in state_of_world) and ('can-show-info-about-the-cases-need-hospitalization' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-the-cases-need-hospitalization'
    if (('started' in state_of_world) and ('can-show-info-about-social-distancing' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-social-distancing'
    if (('started' in state_of_world) and ('can-show-info-about-when-home-isolation-is-necessary' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-when-home-isolation-is-necessasry'
    if (('started' in state_of_world) and ('can-show-info-about-home-isolation' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-home-isolation'
    if (('started' in state_of_world) and ('can-show-info-about-who-is-the-exam-for' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-who-is-the-exam-for'
    if (('started' in state_of_world) and ('can-show-info-about-the-diagnostic-of-the-covid' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-the-diagnostic-of-the-covid'
    if (('started' in state_of_world) and ('can-show-info-about-where-to-get-care' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-where-to-get-care'
    if (('started' in state_of_world) and ('can-show-info-about-should-see-the-doctor' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-should-see-the-doctor'
    if (('started' in state_of_world) and ('can-show-info-riscs' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-the-riscs'
    if (('started' in state_of_world) and ('can-show-info-about-the-risk-group' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-the-risk-group'
    if (('started' in state_of_world) and ('can-show-info-about-worried-about-this-disease' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-worried-about-this-disease'
    if (('started' in state_of_world) and ('can-show-info-about-disease-transmitted-through-the-air' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-disease-transmitted-through-the-air'
    if (('started' in state_of_world) and ('can-show-info-about-disease-spread' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-disease-spread'
    if (('started' in state_of_world) and ('can-show-info-about-disease-present-itself' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-disease-present-itself'
    if (('started' in state_of_world) and ('can-show-info-treatments' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-the-treatments'
    if (('started' in state_of_world) and ('can-show-info-main-symptoms' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-main-symptoms'
    if (('started' in state_of_world) and not('can-go-error-treatment' in state_of_world) and ('can-show-info-protect' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-how-to-protect-from-virus'
    if (('started' in state_of_world) and ('can-show-info-about-health-professional-protection' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-health-professional-protection'
    if (('started' in state_of_world) and ('can-show-info-about-wash-hands-correctly' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-wash-hands-correctly'
    if (('started' in state_of_world) and ('can-show-info-about-homemade-mask-use' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-homemade-mask-use'
    if (('started' in state_of_world) and ('can-show-info-about-homemade-mask-look-like' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-homemade-mask-look-like'
    if (('started' in state_of_world) and ('can-show-info-about-wear-mask' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-wear-mask'
    if (('started' in state_of_world) and ('can-show-info-about-main-prevention-measure' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-main-prevention-measure'
    if (('started' in state_of_world) and ('can-show-info-new-coronavirus' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-about-new-corona-virus'
    if (not('have-patient-days-symptoms' in state_of_world) and ('have-patient-symptoms' in state_of_world) and not('have-diagnostic-system-positive' in state_of_world) and ('can-do-ask-patient-how-many-days-symptoms' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'ask-patient-how-many-days-symptoms'
    if (('started' in state_of_world) and ('can-show-info-mental-health' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('can-back-dialog' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-covid-ce' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-go-error-treatment' in state_of_world) and ('can-show-info-myths-truths-covid' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-the-restrictions-to-buy' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-covid-kill' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-covid-survive-in-surface' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-medicine-for-covid' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-antibiotics-effects' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-people-affected-by-covid' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-pets-spread-covid' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('can-back-dialog' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-go-error-treatment' in state_of_world) and ('can-show-info-when-feel-symptoms' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-the-cases-need-hospitalization' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-social-distancing' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-when-home-isolation-is-necessary' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-home-isolation' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-the-diagnostic-of-the-covid' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-where-to-get-care' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-should-see-the-doctor' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-riscs' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-the-risk-group' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-worried-about-this-disease' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-disease-transmitted-through-the-air' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-disease-spread' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-disease-present-itself' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-treatments' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-main-symptoms' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-go-error-treatment' in state_of_world) and ('can-show-info-about-covid' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-go-error-treatment' in state_of_world) and ('can-show-info-protect' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-health-professional-protection' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-wash-hands-correctly' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-homemade-mask-use' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-homemade-mask-look-like' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-wear-mask' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-about-main-prevention-measure' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (('started' in state_of_world) and ('can-show-info-new-coronavirus' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (not('have-patient-days-symptoms' in state_of_world) and not('have-patient-symptoms' in state_of_world) and not('have-diagnostic-system-positive' in state_of_world) and ('can-do-ask-patient-symptoms' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'ask-patient-symptoms'
    if (not('have-patient-phone-number' in state_of_world) and ('can-do-ask-patient-info-gender' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-gender' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'ask-patient-info-gender'
    if (not('have-patient-phone-number' in state_of_world) and ('can-do-ask-patient-info-gender' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-pregnant-info' in state_of_world) and not('have-patient-gender' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'ask-patient-info-gender'
    if (not('have-patient-days-symptoms' in state_of_world) and ('have-patient-symptoms' in state_of_world) and not('have-diagnostic-system-positive' in state_of_world) and ('can-do-ask-patient-how-many-days-symptoms' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (not('have-patient-days-symptoms' in state_of_world) and not('have-patient-symptoms' in state_of_world) and not('have-diagnostic-system-positive' in state_of_world) and ('can-start-online-service' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'start-online-service'
    if (not('have-patient-phone-number' in state_of_world) and not('have-patient-comorbidities' in state_of_world) and ('can-do-ask-patient-comorbidities' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-gender' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'ask-patient-comorbidities'
    if (not('have-patient-phone-number' in state_of_world) and ('can-do-ask-patient-info-gender' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-gender' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (not('have-patient-days-symptoms' in state_of_world) and not('have-patient-symptoms' in state_of_world) and not('have-diagnostic-system-positive' in state_of_world) and ('can-do-ask-patient-symptoms' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (not('have-patient-phone-number' in state_of_world) and not('have-patient-comorbidities' in state_of_world) and not('have-patient-birthday' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-gender' in state_of_world) and ('can-do-ask-patient-info-birthday' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'ask-patient-info-birthday'
    if (not('have-patient-phone-number' in state_of_world) and not('have-patient-comorbidities' in state_of_world) and ('can-do-ask-patient-comorbidities' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-gender' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (not('have-patient-phone-number' in state_of_world) and not('have-patient-comorbidities' in state_of_world) and not('have-patient-birthday' in state_of_world) and not('have-patient-name' in state_of_world) and not('have-patient-gender-f' in state_of_world) and ('can-do-ask-patient-info-name' in state_of_world) and not('have-patient-gender' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'ask-patient-info-name'
    if (not('have-patient-phone-number' in state_of_world) and not('have-patient-comorbidities' in state_of_world) and not('have-patient-birthday' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-gender' in state_of_world) and ('can-do-ask-patient-info-birthday' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (not('have-patient-phone-number' in state_of_world) and not('have-patient-comorbidities' in state_of_world) and not('have-patient-birthday' in state_of_world) and not('have-patient-name' in state_of_world) and not('have-patient-cpf' in state_of_world) and ('can-do-ask-patient-info-cpf' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-gender' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'ask-patient-info-cpf'
    if (not('have-patient-phone-number' in state_of_world) and not('have-patient-comorbidities' in state_of_world) and not('have-patient-birthday' in state_of_world) and not('have-patient-name' in state_of_world) and not('have-patient-gender-f' in state_of_world) and ('can-do-ask-patient-info-name' in state_of_world) and not('have-patient-gender' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (not('have-patient-phone-number' in state_of_world) and not('have-patient-comorbidities' in state_of_world) and not('have-patient-birthday' in state_of_world) and not('have-patient-name' in state_of_world) and not('have-patient-cpf' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-gender' in state_of_world) and ('can-show-info-calling-health-profitional' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-calling-health-profitional'
    if (not('have-patient-phone-number' in state_of_world) and not('have-patient-comorbidities' in state_of_world) and not('have-patient-birthday' in state_of_world) and not('have-patient-name' in state_of_world) and not('have-patient-cpf' in state_of_world) and ('can-do-ask-patient-info-cpf' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-gender' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
    if (not('have-patient-phone-number' in state_of_world) and not('have-patient-comorbidities' in state_of_world) and not('have-patient-birthday' in state_of_world) and not('have-patient-name' in state_of_world) and not('have-patient-cpf' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-gender' in state_of_world) and not('have-patient-location' in state_of_world) and not('have-patient-postal-code' in state_of_world) and not('can-do-ask-postal-code' in state_of_world) and ('can-do-ask-share-location' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'ask-share-location'
    if (not('have-patient-phone-number' in state_of_world) and not('have-patient-comorbidities' in state_of_world) and not('have-patient-birthday' in state_of_world) and not('have-patient-name' in state_of_world) and not('have-patient-cpf' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-gender' in state_of_world) and not('have-patient-location' in state_of_world) and not('have-patient-postal-code' in state_of_world) and ('can-do-ask-postal-code' in state_of_world) and not('can-do-ask-share-location' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'ask-postal-code'
    if (not('have-patient-phone-number' in state_of_world) and not('have-patient-comorbidities' in state_of_world) and not('have-patient-birthday' in state_of_world) and not('have-patient-name' in state_of_world) and not('have-patient-cpf' in state_of_world) and ('have-diagnostic-system-positive' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-gender' in state_of_world) and ('can-do-show-info-diagnostic-positive' in state_of_world) and not('have-patient-location' in state_of_world) and not('have-patient-postal-code' in state_of_world) and not('can-do-ask-postal-code' in state_of_world) and not('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'show-info-diagnostic-positive'
    if (not('have-patient-phone-number' in state_of_world) and not('have-patient-comorbidities' in state_of_world) and not('have-patient-birthday' in state_of_world) and not('have-patient-name' in state_of_world) and not('have-patient-cpf' in state_of_world) and not('have-patient-gender-f' in state_of_world) and not('have-patient-gender' in state_of_world) and not('have-patient-location' in state_of_world) and not('have-patient-postal-code' in state_of_world) and ('can-do-ask-postal-code' in state_of_world) and not('can-do-ask-share-location' in state_of_world) and ('can-go-error-treatment' in state_of_world) and not('goal' in state_of_world)):
        return 'error-treatment'
