interface StudentStatusBadgeProps {
    status: string;
  }
  
  export default function StudentStatusBadge({
    status,
  }: StudentStatusBadgeProps) {
    const styles: Record<string, string> = {
      ACTIVE: "bg-green-100 text-green-700",
      SUSPENDED: "bg-yellow-100 text-yellow-700",
      WITHDRAWN: "bg-red-100 text-red-700",
      DEACTIVATED: "bg-gray-100 text-gray-700",
      GRADUATED: "bg-blue-100 text-blue-700",
      ALUMNI: "bg-purple-100 text-purple-700",
    };
  
    const labels: Record<string, string> = {
      ACTIVE: "Active",
      SUSPENDED: "Suspended",
      WITHDRAWN: "Withdrawn",
      DEACTIVATED: "Deactivated",
      GRADUATED: "Graduated",
      ALUMNI: "Alumni",
    };
  
    return (
      <span
        className={`rounded-full px-3 py-1 text-xs font-medium ${
          styles[status] || "bg-gray-100 text-gray-700"
        }`}
      >
        {labels[status] || status}
      </span>
    );
  }