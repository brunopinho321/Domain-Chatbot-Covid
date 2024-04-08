(define 
    (domain covid-chatbot)
    (:requirements :non-deterministic :strips :typing :negative-preconditions)
    (:predicates
        (started)
        (user-initiative)
        (have-patient-name)
        (have-patient-cpf)
        (have-patient-birthday)
        (have-patient-comorbidities)
        (have-patient-symptoms)
        (have-patient-days-symptoms)
        (have-patient-location)
        (have-patient-postal-code)
        (have-patient-gender)
        (have-patient-gender-f)
        (have-patient-undeclarete-gender)
        (have-patient-phone-number)
        (have-diagnostic-system)
        (have-patient-undeclarete-location)
        (have-patient-pregnant-info)


        (send-info-name)
        (send-info-cpf)
        (send-info-birthday)
        (send-info-comorbidities)
        (send-info-symptoms)
        (send-info-days-symptoms)
        (send-info-location)
        (send-info-postal-code)
        (send-info-gender)
        (send-info-pregnant-info)
        (send-info-diagnostic-system)
        (send-info-phone-number)
        
        (can-start-online-service)
        

        
        (can-show-info-others)
        (can-show-info-about-covid)
        (can-show-info-mental-health)
        (can-show-info-new-coronavirus)
        (can-show-info-protect)
        (can-show-info-main-symptoms)
        (can-show-info-treatments)
        (can-show-info-riscs)
        (can-show-info-when-feel-symptoms)
        (can-show-info-myths-truths-covid)
        (can-show-info-covid-ce)
       

        (can-do-ask-patient-symptoms)
        (can-do-ask-patient-how-many-days-symptoms)
        (can-do-ask-patient-info-name)
        (can-do-ask-patient-info-cpf)
        (can-do-ask-patient-info-birthday)
        (can-do-ask-patient-comorbidities)
        (can-do-ask-patient-info-gender)
        (can-do-ask-patient-info-pregnant-woman)
        (can-do-ask-patient-info-phone-number)
        (can-do-ask-share-location)
        (can-do-ask-postal-code)

        (can-show-info-about-main-prevention-measure)
        (can-show-info-about-wear-mask)
        (can-show-info-about-homemade-mask-look-like)
        (can-show-info-about-homemade-mask-use)
        (can-show-info-about-wash-hands-correctly)
        (can-show-info-about-health-professional-protection)

        (can-show-info-about-disease-present-itself)
        (can-show-info-about-disease-spread)
        (can-show-info-about-disease-transmitted-through-the-air)
        (can-show-info-about-worried-about-this-disease)
        (can-show-info-about-the-risk-group)
        
        (can-show-info-about-should-see-the-doctor)
        (can-show-info-about-where-to-get-care)
        (can-show-info-about-the-diagnostic-of-the-covid)
        (can-show-info-about-who-is-the-exam-for)
        (can-show-info-about-home-isolation)
        (can-show-info-about-when-home-isolation-is-necessary)
        (can-show-info-about-social-distancing)
        (can-show-info-about-the-cases-need-hospitalization)

        (can-show-info-about-pets-spread-covid)
        (can-show-info-about-people-affected-by-covid)
        (can-show-info-about-antibiotics-effects)
        (can-show-info-about-medicine-for-covid)
        (can-show-info-about-covid-survive-in-surface)
        (can-show-info-about-covid-kill)
        (can-show-info-about-the-restrictions-to-buy)

        
        
        (can-call-diagnostic-system)
        (can-show-ask-user-grade)
        (can-do-start-dialog)
        (can-back-dialog)
        (send-grade)
        (have-patient-grade)

        (can-go-error-treatment)

        (can-do-human-take-control-dialog)
        
        (goal)
    )

    (:action show-welcome-message
        :parameters ()
        :precondition (and 
            (user-initiative)
            (not (started))
        )
        :effect(oneof
            ;outcome welcome-message
            (and 
                (started)
                (can-do-start-dialog)
                (not (user-initiative))
            )
        )
    )



    (:action start-dialog
        :parameters ()
        :precondition (and 
            (started)
            (can-do-start-dialog)
            (not(can-go-error-treatment))
            ;(can-back-dialog)
            
        )
        :effect (oneof 
            ;outcome 1online-service
            (and 
                (can-start-online-service)
                (not (can-do-start-dialog))
                (not (can-back-dialog))
            )
            ;outcome 2information-about-covid
            (and 
                (can-show-info-about-covid)
                (not (can-do-start-dialog))
                (not (can-back-dialog))
            )
            ;outcome 3mental-health-care
            (and 
                (can-show-info-mental-health)
                (not (can-do-start-dialog))
                (not (can-back-dialog))
            )
            ;outcome 4choose-others
            (and 
                (can-show-info-others)
                (not (can-do-start-dialog))
                (not (can-back-dialog))
            )
            ;outcome Error
            (and 
                (can-do-start-dialog)
                (can-go-error-treatment)
            )
        )
    )
    
    (:action error-treatment
        :parameters ()
        :precondition (and (can-go-error-treatment))
        :effect (oneof
            ;outcome error-treatment
            (and 
                (not(can-go-error-treatment))
            )
        )   
    )
    

    (:action start-online-service
        :parameters ()
        :precondition (and 
            (can-start-online-service)
            (not(can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome online-service
            (and 
                (not (can-start-online-service))
                (can-do-ask-patient-symptoms)
            )
        )
    )

     (:action ask-patient-symptoms
        :parameters ()
        :precondition (and 
            (can-do-ask-patient-symptoms) 
            (not(have-patient-symptoms))
            (not(can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome have-symptoms-info
            (and 
                (send-info-symptoms)
                (have-patient-symptoms)
                (can-do-ask-patient-how-many-days-symptoms)
                (not(can-do-ask-patient-symptoms))
            )
            ;outcome Error
            (and 
                (can-do-ask-patient-symptoms)
                (not(have-patient-symptoms))
                (not(send-info-symptoms))
                (can-go-error-treatment)
            )
        )  
    )

    (:action  ask-patient-how-many-days-symptoms
        :parameters ()
        :precondition (and
            ;(have-patient-symptoms)
            (can-do-ask-patient-how-many-days-symptoms)
            (not (have-patient-days-symptoms))
            (not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome have-days-symptoms
            (and
                (send-info-days-symptoms)
                (have-patient-days-symptoms)
                (can-call-diagnostic-system)
                (not(can-do-ask-patient-how-many-days-symptoms))                
            )
            ;outcome Error
            (and
                (not(send-info-days-symptoms))
                (can-do-ask-patient-how-many-days-symptoms)
                (not (have-patient-days-symptoms))
                (can-go-error-treatment)   
            )
        )
    )



    (:action call-diagnostic-system
        :parameters ()
        :precondition (and 
            (can-call-diagnostic-system) 
            (not(have-diagnostic-system))
            (not(can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome patient-with-covid
            (and
                (send-info-diagnostic-system)
                (not (can-call-diagnostic-system)) 
                (have-diagnostic-system)
                (can-do-ask-share-location)
            )
            ;outcome to-the-end-service
            (and
                (send-info-diagnostic-system)
                (not (have-diagnostic-system)) 
                (can-show-ask-user-grade)
                (not (can-call-diagnostic-system))
            )
        )
    )

    (:action ask-share-location
        :parameters ()
        :precondition (and 
            (can-do-ask-share-location)
            (not(can-do-ask-postal-code))
            (not(have-patient-location))
            (not(have-patient-postal-code))
            (not(can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome not-have-share-location
            (and 
                (send-info-location)
                (have-patient-undeclarete-location)
                (not (can-do-ask-share-location))
                (not(have-patient-location))
                (can-do-ask-postal-code)
            )
            ;outcome have-share-location
            (and 
                (not (can-do-ask-share-location))
                (can-do-ask-patient-info-cpf)
                (have-patient-location)
                (send-info-location)
            )
        )
        
    )

    (:action ask-postal-code
        :parameters ()
        :precondition (and 
            (can-do-ask-postal-code)
            (not(have-patient-location))
            (not(can-do-ask-share-location))
            (not(have-patient-postal-code))
            (not(can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome have-postal-code
            (and 
                (send-info-postal-code)
                (not (can-do-ask-postal-code))
                (have-patient-postal-code)
                (can-do-ask-patient-info-cpf)
            )
            ;outcome Error
            (and 
                (not(send-info-postal-code))
                (can-do-ask-postal-code)
                (not(have-patient-location))
                (not(can-do-ask-share-location))
                (not(have-patient-postal-code))
                (can-go-error-treatment)
            )
        )
    )

    (:action ask-patient-info-cpf
        :parameters ()
        :precondition (and 
            (can-do-ask-patient-info-cpf)
            (not(have-patient-cpf))
            (not(can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome have-patient-cpf
            (and 
                (send-info-cpf)
                (not(can-do-ask-patient-info-cpf))
                (have-patient-cpf)
                (can-do-ask-patient-info-name)
            )
            ;outcome Error
            (and 
                (not(send-info-cpf))
            	(can-do-ask-patient-info-cpf)
                (not(have-patient-cpf))
                (can-go-error-treatment)
            )
        )
    )

    (:action ask-patient-info-name
        :parameters ()
        :precondition (and 
            (can-do-ask-patient-info-name)
            (not(have-patient-name))
            (not(can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome have-patient-name
            (and 
                (send-info-name)
                (have-patient-name)
                (can-do-ask-patient-info-birthday)
            )
            ;outcome Error 
            (and 
                (not(send-info-name))
            	(can-do-ask-patient-info-name)
                (not(have-patient-name))
                (can-go-error-treatment)
            )
        )
    )

    (:action ask-patient-info-birthday
        :parameters ()
        :precondition (and 
            (can-do-ask-patient-info-birthday)
            (not(have-patient-birthday))
            (not (can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome have-patient-birthday
            (and 
                (have-patient-birthday)
                (send-info-birthday)
                (can-do-ask-patient-comorbidities)
            )
            ;outcome Error
            (and 
                (not(send-info-birthday))
            	(can-do-ask-patient-info-birthday)
                (not(have-patient-birthday))
                (can-go-error-treatment)
            )
        )
    )
 
    (:action ask-patient-comorbidities
        :parameters ()
        :precondition (and 
            (can-do-ask-patient-comorbidities)
            (not(have-patient-comorbidities))
            (not (can-go-error-treatment))
            
        )
        :effect (oneof 
            ;outcome have-comorbidities
            (and 
                (have-patient-comorbidities) 
                (can-do-ask-patient-info-gender)
                (send-info-comorbidities)
            )
            ;outcome Error
            (and 
            	(can-do-ask-patient-comorbidities)
                (not(have-patient-comorbidities))
                (not(send-info-comorbidities))
                (can-go-error-treatment)
            )
        )
    )
    
    (:action ask-patient-info-gender
        :parameters ()
        :precondition (and 
            (can-do-ask-patient-info-gender)
            (not(have-patient-gender)) 
            (not(have-patient-gender-f))
            (not(can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome have-gender
            (and 
                (have-patient-gender)
                (send-info-gender)
                (not (have-patient-gender-f))
                (can-do-ask-patient-info-phone-number)   
            )
            ;outcome have-undeclarte-gender
            (and
                (have-patient-undeclarete-gender)
                (not (have-patient-gender-f))
                (not (have-patient-gender))
                (can-do-ask-paient-info-phone-number)
            )
            ;outcome have-gender-f
            (and 
                (have-patient-gender)
                (have-patient-gender-f)
                (not (have-patient-undeclarete-gender))
                (send-info-gender)
                (can-do-ask-patient-info-pregnant-woman)
            )
            ;outcome Error
            (and 
                (not(send-info-gender))
            	(can-do-ask-patient-info-gender)
                (not(have-patient-gender)) 
                (not(have-patient-gender-f))
                (can-go-error-treatment)

            )
        )
    )

    (:action ask-patient-info-pregmant-woman
        :parameters ()
        :precondition (and 
            (can-do-ask-patient-info-pregnant-woman)
            (not(have-patient-pregnant-info))
            (not (can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome have-patient-info-pregnant
            (and 
                (have-patient-pregnant-info)
                (send-info-pregnant-info)
                (can-do-ask-patient-info-phone-number)
            )
            ;outcome Error
            (and 
            	(can-do-ask-patient-info-pregnant-woman)
                (not(have-patient-pregnant-info))
                (can-go-error-treatment)
                (not(send-info-pregnant-info))
            )
        )
    )

    (:action ask-patient-info-phone-number
        :parameters ()
        :precondition (and 
            (can-do-ask-patient-info-phone-number)
            (not(have-patient-phone-number))
            (not (can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome have-patient-info-phone
            (and 
                (send-info-phone-number)
                (have-patient-phone-number)
                (can-do-human-take-control-dialog)
            )
            ;outcome Error
            (and
                (not(send-info-phone-number))  
            	(can-do-ask-patient-info-phone-number)
                (not(have-patient-phone-number))
                (can-go-error-treatment)
            )
        )
    )
   
     (:action health-agent-takes-control
        :parameters ()
        :precondition (and (can-do-human-take-control-dialog)
       		(not(can-go-error-treatment))	
       	)
        :effect (oneof 
            ;outcome another-human-control-the-dialog
            (and 
                (can-do-human-take-control-dialog)
            )

            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
            	(not (can-do-human-take-control-dialog))
            )
        )
    )

    (:action show-info-mental-health
        :parameters ()
        :precondition (and (can-show-info-mental-health)
            (not (can-back-dialog))
            (not(can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
                (not (can-show-info-mental-health))
            )
            ;outcome come-back
            (and 
                (can-do-start-dialog) 
                (not(can-show-info-mental-health))
                (can-back-dialog)
            )
            ;outcome Error
            (and 
                (can-show-info-mental-health)
                (not (can-back-dialog))
                (can-go-error-treatment)

            ) 
        )
    )
    
    (:action show-info-about-covid
        :parameters ()
        :precondition (and 
            (can-show-info-about-covid)
            (not(can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome 1-what-is-the-new-coronavirus?
            (and 
                (can-show-info-new-coronavirus)
                (not (can-show-info-about-covid))
            )
            ;outcome 2-how-do-I-protect-myself
            (and 
                (can-show-info-protect)
                (not (can-show-info-about-covid))
            )
            ;outcome 3-what-are-the-main-symptoms
            (and 
                (can-show-info-main-symptoms)
                (not (can-show-info-about-covid))
            )
            ;outcome 4-what-are-the-treatments
            (and 
                (can-show-info-treatments)
                (not (can-show-info-about-covid))
            )
            ;outcome 5-what-are-the-riscs
            (and 
                (can-show-info-riscs)
                (not (can-show-info-about-covid))
            )
            ;outcome 6-what-to-do-when-feel-the-symptoms
            (and 
                (can-show-info-when-feel-symptoms)
                (not (can-show-info-about-covid))
            )
            ;outcome 7-myths-and-truths-about-covid
            (and 
                (can-show-info-myths-truths-covid)
                (not (can-show-info-about-covid))
            )
            ;outcome 8-information-about-covid-in-ceara
            (and 
                (can-show-info-covid-ce)
                (not (can-show-info-about-covid))
            )
            ;outcome 9-to-end-the-service
            (and 
                (can-show-ask-user-grade) 
                (not (can-show-info-about-covid))
            )
            ;outcome Error
            (and 
                (can-go-error-treatment)
                (can-show-info-about-covid)
            )
        )
    )

    (:action show-info-about-new-corona-virus
        :parameters ()
        :precondition (and (can-show-info-new-coronavirus)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (started)
                (can-do-start-dialog)
                (can-back-dialog)
                (not(can-go-error-treatment))
                (not (can-show-info-new-coronavirus))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
                (not (can-show-info-new-coronavirus))
            )
        )
    )



    (:action show-info-about-main-symptoms
        :parameters ()
        :precondition (and (can-show-info-main-symptoms)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not(can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-main-symptoms))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
                (not (can-show-info-main-symptoms))
            )
        )
    )

    (:action show-info-about-the-treatments
        :parameters ()
        :precondition (and (can-show-info-treatments)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not(can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-treatments))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-treatments))
            )
        )
    )
    

    (:action show-info-about-covid-in-ceara
        :parameters ()
        :precondition (and (can-show-info-covid-ce)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not(can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-covid-ce))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-covid-ce))
            )
        )
    )

    
    (:action show-info-about-how-to-protect-from-virus
        :parameters ()
        :precondition (and (can-show-info-protect)
                            (not (can-go-error-treatment))
        )
        :effect (oneof
            ;outcome 1-what-are-the-main-prevention-measure
            (and 
                (can-show-info-about-main-prevention-measure)
                (not(can-show-info-protect))
            )
            ;outcome 2-should-i-wear-mask
            (and 
                (can-show-info-about-wear-mask)
                (not(can-show-info-protect))
            )
            ;outcome 3-what-should-my-homemade-mask-look-like
            (and 
                (can-show-info-about-homemade-mask-look-like)
                (not(can-show-info-protect))
            )
            ;outcome 4-can-i-use-my-homemade-mask-more-than-once
            (and 
                (can-show-info-about-homemade-mask-use)
                (not(can-show-info-protect))
            )
            ;outcome 5-how-to-wash-your-hands-correctly
            (and 
                (can-show-info-about-wash-hands-correctly)
                (not(can-show-info-protect))
            )
            ;outcome 6-how-health-professional-can-protect-themselves-from-covid
            (and 
                (can-show-info-about-health-professional-protection)
                (not(can-show-info-protect))
            )
        )
    )

    (:action show-info-about-main-prevention-measure
        :parameters ()
        :precondition (and (can-show-info-about-main-prevention-measure)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not(can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-main-prevention-measure))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
                (not (can-show-info-about-main-prevention-measure))
            )
        )
    )
    
    (:action show-info-about-wear-mask
        :parameters ()
        :precondition (and (can-show-info-about-wear-mask)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not(can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-wear-mask))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
                (not (can-show-info-about-wear-mask))
            )
        )
    )
    
    (:action show-info-about-homemade-mask-look-like
        :parameters ()
        :precondition (and (can-show-info-about-homemade-mask-look-like)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-homemade-mask-look-like))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-about-homemade-mask-look-like))
            )
        )
    )

    (:action show-info-about-homemade-mask-use
        :parameters ()
        :precondition (and (can-show-info-about-homemade-mask-use)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-homemade-mask-use))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
                (not (can-show-info-about-homemade-mask-use))
            )
        )
    )
    
    (:action show-info-about-wash-hands-correctly
        :parameters ()
        :precondition (and (can-show-info-about-wash-hands-correctly)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
           
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-about-wash-hands-correctly))
            )

             ;outcome come-back
            (and 
                (started)  
                (can-do-start-dialog)
                (not(can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-wash-hands-correctly))
            )
        )
    )

    (:action show-info-about-health-professional-protection
        :parameters ()
        :precondition (and (can-show-info-about-health-professional-protection)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-health-professional-protection))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-about-health-professional-protection))
            )
        )
    )
    
    
    (:action show-info-about-the-riscs
        :parameters ()
        :precondition (and (can-show-info-riscs)
                            (not (can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome 1-how-does-this-disease-present-itself
            (and
                (can-show-info-about-disease-present-itself)
                (not (can-show-info-riscs))
            )
            ;outcome 2-how-does-this-disease-spread
            (and
                (can-show-info-about-disease-spread)
                (not (can-show-info-riscs))
            )
            ;outcome 3-is-this-disease-transmitted-through-the-air
            (and
                (can-show-info-about-disease-transmitted-through-the-air)
                (not (can-show-info-riscs))
            )
            ;outcome 4-should-i-be-worried-about-this-disease
            (and
                (can-show-info-about-worried-about-this-disease)
                (not (can-show-info-riscs))
            )
            ;outcome 5-who-are-the-risk-group
            (and
                (can-show-info-about-the-risk-group)
                (not (can-show-info-riscs))
            )
            ;outcome Error
            (and 
                (can-go-error-treatment)
                (can-show-info-riscs)
            )
        )
    )

    (:action show-info-about-disease-present-itself
        :parameters ()
        :precondition (and (can-show-info-about-disease-present-itself)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-disease-present-itself))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-about-disease-present-itself))
            )
        )
    )

    (:action show-info-about-disease-spread
        :parameters ()
        :precondition (and (can-show-info-about-disease-spread)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-disease-spread))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
                (not (can-show-info-about-disease-spread))
            )
        )
    )
    
    (:action show-info-about-disease-transmitted-through-the-air
        :parameters ()
        :precondition (and (can-show-info-about-disease-transmitted-through-the-air)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-disease-transmitted-through-the-air))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-about-disease-transmitted-through-the-air))
            )
        )
    )
    
    (:action show-info-about-worried-about-this-disease
        :parameters ()
        :precondition (and (can-show-info-about-worried-about-this-disease)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-worried-about-this-disease))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-about-worried-about-this-disease))
            )
        )
    )

    (:action show-info-about-the-risk-group
        :parameters ()
        :precondition (and (can-show-info-about-the-risk-group)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-the-risk-group))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-about-the-risk-group))
            )
        )
    )

    
    (:action show-info-about-when-feel-the-symptoms
        :parameters ()
        :precondition (and (can-show-info-when-feel-symptoms) 
                            (not (can-go-error-treatment))
        )
        :effect (oneof 
            ;outcome 1-i-dont-feel-well-shold-i-see-a-doctor
            (and
                (can-show-info-about-should-see-the-doctor)
                (not (can-show-info-when-feel-symptoms)) 
            )
            ;outcome 2-where-to-get-care
            (and
                (can-show-info-about-where-to-get-care)
                (not (can-show-info-when-feel-symptoms))
            )
            ;outcome 3-how-is-the-diagnosis-of-the-covid
            (and
                (can-show-info-about-the-diagnostic-of-the-covid)
                (not (can-show-info-when-feel-symptoms))
            )
            ;outcome 4-who-is-the-exam-for
            (and 
                (can-show-info-about-who-is-the-exam-for)
                (not (can-show-info-when-feel-symptoms))
            )
            ;outcome 5-what-is-home-isolation
            (and
                (can-show-info-about-home-isolation)
                (not (can-show-info-when-feel-symptoms))
            )
            ;outcome 6-when-is-home-isolation-is-necessary
            (and
                (can-show-info-about-when-home-isolation-is-necessary)
                (not (can-show-info-when-feel-symptoms))
            )
            ;outcome 7-what-is-social-distancing
            (and
                (can-show-info-about-social-distancing)
                (not (can-show-info-when-feel-symptoms))
            )
            ;outcome 8-which-cases-need-hospitalization
            (and
                (can-show-info-about-the-cases-need-hospitalization)
                (not (can-show-info-when-feel-symptoms))
            )
            
            ;outcome Error
            (and 
                (can-go-error-treatment)
                (can-show-info-when-feel-symptoms)
            )

        )

    )

    (:action show-info-about-should-see-the-doctor
        :parameters ()
        :precondition (and (can-show-info-about-should-see-the-doctor)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-should-see-the-doctor))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-about-should-see-the-doctor))
            )
        )
    )

    (:action show-info-about-where-to-get-care
        :parameters ()
        :precondition (and (can-show-info-about-where-to-get-care)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-where-to-get-care))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-about-where-to-get-care))
            )
        )
    )

    (:action show-info-about-the-diagnostic-of-the-covid
        :parameters ()
        :precondition (and (can-show-info-about-the-diagnostic-of-the-covid)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-the-diagnostic-of-the-covid))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-about-the-diagnostic-of-the-covid))
            )
        )
    )

    (:action show-info-about-who-is-the-exam-for
        :parameters ()
        :precondition (and (can-show-info-about-who-is-the-exam-for))
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-who-is-the-exam-for))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-about-who-is-the-exam-for))
            )
        )
    )

    (:action show-info-about-home-isolation
        :parameters ()
        :precondition (and (can-show-info-about-home-isolation))
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-home-isolation))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-about-home-isolation))
            )
        )
    )
    
    (:action show-info-about-when-home-isolation-is-necessasry
        :parameters ()
        :precondition (and (can-show-info-about-when-home-isolation-is-necessary)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-when-home-isolation-is-necessary))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-about-when-home-isolation-is-necessary))
            )
        )
    )

    (:action show-info-about-social-distancing
        :parameters ()
        :precondition (and (can-show-info-about-social-distancing)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-social-distancing))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
            )
        )
    )

    (:action show-info-about-the-cases-need-hospitalization
        :parameters ()
        :precondition (and (can-show-info-about-the-cases-need-hospitalization)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-the-cases-need-hospitalization))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
            )
        )
    )

    
    (:action show-info-about-myths-and-truths
        :parameters ()
        :precondition (and (can-show-info-myths-truths-covid)
                            (not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome 1-can-pets-spread-covid
            (and
                (can-show-info-about-pets-spread-covid)
                (not (can-show-info-myths-truths-covid))
            )
            ;outcome 2-who-are-the-people-most-affected-by-covid
            (and
                (can-show-info-about-people-affected-by-covid)
                (not (can-show-info-myths-truths-covid))
            )
            ;outcome 3-are-antibiotics-effective-against-covid
            (and
                (can-show-info-about-antibiotics-effects)
                (not (can-show-info-myths-truths-covid))
            )
            ;outcome 4-can-i-take-any-medicine-for-covid
            (and
                (can-show-info-about-medicine-for-covid)
                (not (can-show-info-myths-truths-covid))
            )
            ;outcome 5-how-longer-does-the-covid-survive-in-surfaces
            (and 
                (can-show-info-about-covid-survive-in-surface)
                (not (can-show-info-myths-truths-covid))
            )
            ;outcome 6-can-covid-kill
            (and
                (can-show-info-about-covid-kill)
                (not (can-show-info-myths-truths-covid))
            )
            ;outcome 7-are-there-restrictions-to-buy
            (and
                (can-show-info-about-the-restrictions-to-buy)
                (not (can-show-info-myths-truths-covid))
            )
            ;outcome Error
            (and 
                (can-go-error-treatment)
                (can-show-info-myths-truths-covid)
            )    
        )
    )

    (:action show-info-about-pets-spread-covid
        :parameters ()
        :precondition (and (can-show-info-about-pets-spread-covid)
        	(not(can-go-error-treatment))
        )
        :effect (and 
            ;outcome come-back
            (and (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-pets-spread-covid))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
                (not (can-show-info-about-pets-spread-covid))
            )
        )
    )

    (:action show-info-about-people-affected-by-covid
        :parameters ()
        :precondition (and (can-show-info-about-people-affected-by-covid)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-people-affected-by-covid))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
                (not (can-show-info-about-people-affected-by-covid))
            )
        )
    )

    (:action show-info-about-antibiotics-effects
        :parameters ()
        :precondition (and (can-show-info-about-antibiotics-effects)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-antibiotics-effects))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
                (not (can-show-info-about-antibiotics-effects))
            )
        )
    )

    (:action show-info-about-medicine-for-covid
        :parameters ()
        :precondition (and (can-show-info-about-medicine-for-covid)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-medicine-for-covid))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
                (not (can-show-info-about-medicine-for-covid))
            )
        )
    )

    (:action show-info-about-covid-survive-in-surface
        :parameters ()
        :precondition (and (can-show-info-about-covid-survive-in-surface)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-covid-survive-in-surface))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
                (not (can-show-info-about-covid-survive-in-surface))
            )
        )
    )
    
    (:action show-info-about-covid-kill
        :parameters ()
        :precondition (and (can-show-info-about-covid-kill)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-covid-kill))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-about-covid-kill)) 
            )
        )
    )

    (:action show-info-about-the-restrictions-to-buy
        :parameters ()
        :precondition (and (can-show-info-about-the-restrictions-to-buy)
        	(not(can-go-error-treatment))
        )
        :effect (oneof
            ;outcome come-back
            (and 
                (can-do-start-dialog)
                (not (can-go-error-treatment))
                (can-back-dialog)
                (not (can-show-info-about-the-restrictions-to-buy))
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
                (not (can-show-info-about-the-restrictions-to-buy))
            )
        )
    )



    (:action show-info-others
        :parameters ()
        :precondition (and 
            (can-show-info-others)
            (not(can-do-start-dialog))
            (not(can-go-error-treatment))
            (not (can-back-dialog))
        )
        :effect (oneof 
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade)
                (not (can-show-info-others))

            )
            ;outcome come-back
            (and                 
                (not (can-show-info-others))
                (not (can-go-error-treatment))
                (started)
                (can-do-start-dialog)
                (can-back-dialog)
            )
            ;outcome to-end-your-service
            (and 
                (can-show-ask-user-grade) 
                (can-show-info-others)
            )
        )
    )

   
    (:action ask-user-grade
        :parameters ()
        :precondition (and (can-show-ask-user-grade) 
                            (not(goal))
                            (not(can-go-error-treatment))
                            
        )
        :effect (oneof  
            ;outcome finish-service
            (and 
                (have-patient-grade)
                (not (can-show-ask-user-grade)) 
            )

            ;outcome Error
            (and 
            	(can-go-error-treatment)
                (can-show-ask-user-grade)
            )
        
        )
    )

    (:action finish-service
        :parameters ()
        :precondition (and (send-grade)
            (not(goal))
        )
        :effect (oneof
            ;outcome finish
            (and
                (goal)
            )
        )
    )
    
)