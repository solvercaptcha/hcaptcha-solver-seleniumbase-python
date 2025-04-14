**Frequently Asked Questions Regarding hCaptcha Solving**

1. **Captcha takes too long to solve**  
   **Answer:** hCaptcha may take longer to solve than standard text or graphical captchas. The delays are due to both the complexity of the challenges and the need to wait for an operator's response or a spot in the service's queue.

2. **I receive the `ERROR_CAPTCHA_UNSOLVABLE` error**  
   **Explanation:**  
   The high complexity of the images can lead to recognition errors - an operator might misinterpret the challenge or the algorithm might err. A small percentage of `ERROR_CAPTCHA_UNSOLVABLE` errors is normal. However, if this error occurs every time, it most likely indicates that the captcha parameters provided are incorrect.  
   **Recommended actions:**  
   - If only a few errors occur, consider it normal.  
   - If the error appears consistently, double-check the captcha parameters being sent.

3. **Compatibility with web applications**  
   **Explanation:**  
   Some websites use additional dynamic logic or behavioral checks to determine whether a request is automated. As a result, even if the captcha is solved correctly, the site might suspect the use of a third-party service and take additional measures (such as blocking).  
   **Answer:** If you experience issues with using the obtained token, we recommend using alternative methods for solving hCaptcha. More details on these methods can be found in the section "What are the other ways to solve hCaptcha?"

4. **I receive a resource block after solving the captcha**  
   **Explanation:**  
   Some websites may track IP addresses or behavior patterns associated with captcha-solving services. When a site detects the use of a third-party service, it may strengthen its verification measures or restrict access altogether.

5. **Additional Verification**  
   **Explanation:**  
   In cases of repeated errors or suspicious activity, the site might require further verification (such as multi-step authentication), which negatively affects the efficiency of these services.

6. **I can't figure out how to use the obtained token on the page**  
   **Recommended actions:**  
   - Contact our technical support - there might be an existing solution available.  
   - Alternatively, you can use an alternative approach to solving hCaptcha that does not require applying the token directly on the page. More details are provided in the corresponding section.

7. **What are the other ways to solve hCaptcha?**  
   There are three main approaches:
   - Solving using a [token method](https://solvecaptcha.com/captcha-solver-api#solving_hcaptcha).
   - Solving using the [Grid method](https://solvecaptcha.com/captcha-solver-api#solving_grid).
   - Solving using the [Coordinates method](https://solvecaptcha.com/captcha-solver-api#solving_clickcaptcha) .

   **Note:**  
   The Grid and Coordinates methods are more difficult to automate, but they are often more effective as they do not rely on the standard token application logic. To use these methods, you need to employ browser automation: manually click on the captcha, capture the images, send them to the service, and then click on the corresponding coordinates.


8. **Do you have a script for automatically retrieving hCaptcha images?**  
   **Answer:** Yes, we do have one. The script is available at Gist: [hcaptcha-img-extractor.js](https://gist.github.com/solvecaptcha-com/e8ac3b1b9fceb9f3e12003113f50c2e5)


If you have any additional questions or issues related to solving hCaptcha, please contact our technical support:

<a href="mailto:info@solvecaptcha.com"><img src="https://github.com/user-attachments/assets/539df209-7c85-4fa5-84b4-fc22ab93fac7" width="80" height="30"></a>
<a href="https://solvecaptcha.com/support/faq#create-ticket"><img src="https://github.com/user-attachments/assets/be044db5-2e67-46c6-8c81-04b78bd99650" width="81" height="30"></a>
   