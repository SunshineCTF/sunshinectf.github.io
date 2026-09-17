// Keep the published UTC schedule readable even when localization is unavailable.
(() => {
  try {
    const formatter = new Intl.DateTimeFormat(undefined, {
      year: "numeric",
      month: "short",
      day: "numeric",
      hour: "numeric",
      minute: "2-digit",
      timeZoneName: "short",
    });

    document.querySelectorAll(".event-dates time[datetime]").forEach((time) => {
      const date = new Date(time.dateTime);
      if (Number.isNaN(date.getTime())) return;

      const localTime = document.createElement("span");
      localTime.className = "local-time";
      localTime.textContent = `Your time: ${formatter.format(date)}`;
      time.after(localTime);
    });
  } catch {
    // The original UTC times remain the authoritative fallback.
  }
})();
