using System.Text.RegularExpressions;

public class DomainNameValidator
{
    public bool validate(string domain)
    {
        var pattern = @"^(([a-z\d][a-z\d-]{0,61}[a-z\d]|[a-z\d])\.){1,127}(?!-)[a-z\d-]*[a-z-][a-z\d-]*(?<!-)$";

        return domain.Length < 254 && Regex.IsMatch(domain, pattern, RegexOptions.IgnoreCase);
    }
}