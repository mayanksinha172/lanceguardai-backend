import os
import threading
import resend

RESEND_API_KEY = os.getenv("RESEND_API_KEY", "")


def _send(to_email: str, name: str, position: int) -> None:
    if not RESEND_API_KEY:
        print("Email skipped: RESEND_API_KEY not set")
        return

    resend.api_key = RESEND_API_KEY
    first = name.split()[0] if name else "there"

    html = f"""
<!DOCTYPE html>
<html>
<body style="margin:0;padding:0;background:#000000;font-family:'Inter',Arial,sans-serif;-webkit-font-smoothing:antialiased">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#000000;padding:40px 20px">
    <tr><td align="center">
      <table width="520" cellpadding="0" cellspacing="0" style="max-width:520px;width:100%">

        <tr><td style="padding-bottom:32px">
          <span style="font-size:11px;color:#11ff99;font-weight:600;letter-spacing:0.1em;text-transform:uppercase">
            FreelanceGuard AI
          </span>
        </td></tr>

        <tr><td style="padding-bottom:16px">
          <h1 style="margin:0;font-size:30px;font-weight:400;line-height:1.2;color:#fcfdff">
            You're #<span style="color:#11ff99">{position}</span> on the list, {first}.
          </h1>
        </td></tr>

        <tr><td style="padding-bottom:16px">
          <p style="margin:0;font-size:16px;line-height:1.7;color:rgba(252,253,255,0.65)">
            We got you. When we launch, you'll be among the first to know — and as an early member,
            you're locked in for <strong style="color:#11ff99">3 months free</strong>.
          </p>
        </td></tr>

        <tr><td style="padding-bottom:32px">
          <p style="margin:0;font-size:15px;line-height:1.7;color:rgba(252,253,255,0.55)">
            FreelanceGuard AI writes proposals in under 60 seconds, detects scope creep in real time,
            and auto-generates priced change orders — so every hour of work gets paid.
          </p>
        </td></tr>

        <tr><td style="border-top:1px solid rgba(255,255,255,0.08);padding-top:24px">
          <p style="margin:0;font-size:11px;color:#464a4d;line-height:1.6">
            You're receiving this because you joined the FreelanceGuard AI waitlist.<br>
            No spam ever. Reply to unsubscribe.
          </p>
        </td></tr>

      </table>
    </td></tr>
  </table>
</body>
</html>
"""

    try:
        resend.Emails.send({
            "from": "FreelanceGuard AI <onboarding@resend.dev>",
            "to": [to_email],
            "subject": f"You're in, {first} — FreelanceGuard AI",
            "html": html,
        })
        print(f"Welcome email sent to {to_email}")
    except Exception as exc:
        print(f"Email send failed for {to_email}: {exc}")


def send_welcome_email(to_email: str, name: str, position: int) -> None:
    thread = threading.Thread(target=_send, args=(to_email, name, position), daemon=True)
    thread.start()
